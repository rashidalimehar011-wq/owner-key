#!/usr/bin/env python3
# YouTube Trend Analyzer - By: Rashid Ali Mehar

import sys
import requests
from datetime import datetime

# ═══ APPROVAL CHECK ═══
sys.path.insert(0, ".")
try:
    from check_approval import verify
    verify()
except ImportError:
    print("⚠️  Approval system nahi mila")
    print("   Chalao: python check_approval.py")
    sys.exit(1)
# ═════════════════════

API_KEY = "AIzaSyBZos08xMm6VrgWjFENRzEq60vhPuuItX0"

BANNER = """
=======================================
   YOUTUBE TREND ANALYZER
   By: Rashid Ali Mehar
=======================================
"""

def get_trending():
    print(BANNER)
    print(f"Fetching... {datetime.now().strftime('%d %b %Y, %I:%M %p')}")
    print("Region: Pakistan\n")
    
    url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "part": "snippet,statistics",
        "chart": "mostPopular",
        "regionCode": "PK",
        "maxResults": 10,
        "key": API_KEY
    }
    
    try:
        response = requests.get(url, params=params, timeout=15)
        data = response.json()
        
        if "error" in data:
            print(f"API Error: {data['error']['message']}")
            return
        
        items = data.get("items", [])
        if not items:
            print("Koi video nahi mili.")
            return
        
        print(f"{'#':<3}{'Title':<45}{'Views'}")
        print("-" * 70)
        
        for i, item in enumerate(items, 1):
            title = item["snippet"]["title"]
            views = int(item["statistics"].get("viewCount", 0))
            if len(title) > 42:
                title = title[:39] + "..."
            if views >= 1000000:
                v = f"{views/1000000:.1f}M"
            elif views >= 1000:
                v = f"{views/1000:.0f}K"
            else:
                v = str(views)
            print(f"{i:<3}{title:<45}{v}")
        
        print("\n" + "=" * 70)
        print("Complete!")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_trending()
