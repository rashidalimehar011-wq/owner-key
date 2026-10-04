import requests, time, os, sys
from datetime import datetime

API_KEY = "AIzaSyAKT94Ep_Ad6E_Pfi1sX54Zt1GPrNnyxBc"

CATEGORIES = {
    "1": {"name": "Movies", "query": "pakistani movie trailer"},
    "2": {"name": "Songs", "query": "pakistani song music"},
    "3": {"name": "Naats", "query": "naat sharif urdu"},
    "4": {"name": "Kids", "query": "kids cartoon urdu"},
    "5": {"name": "Qawwali", "query": "qawwali"},
    "6": {"name": "Comedy", "query": "comedy funny"},
    "7": {"name": "Gaming", "query": "gaming pubg minecraft"},
    "8": {"name": "News", "query": "pakistan news"},
}

def clear():
    os.system("clear")

def show_menu():
    clear()
    print("=" * 50)
    print("   YOUTUBE CATEGORY MONITOR")
    print("   By: Rashid Ali Mehar")
    print("=" * 50)
    print("")
    print("Apni category chuno:\n")
    for key, cat in CATEGORIES.items():
        print(f"   [{key}] {cat['name']}")
    print("\n   [0] Exit")
    print("-" * 50)

def search_yt(query):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {"part": "snippet", "q": query, "type": "video",
              "regionCode": "PK", "maxResults": 5, "key": API_KEY}
    try:
        r = requests.get(url, params=params, timeout=15)
        data = r.json()
        if "error" in data:
            print(f"API Error: {data['error']['message']}")
            return None
        items = data.get("items", [])
        ids = [i["id"]["videoId"] for i in items if "videoId" in i.get("id", {})]
        if not ids:
            return []
        url2 = "https://www.googleapis.com/youtube/v3/videos"
        p2 = {"part": "snippet,statistics", "id": ",".join(ids), "key": API_KEY}
        r2 = requests.get(url2, params=p2, timeout=15)
        return r2.json().get("items", [])
    except Exception as e:
        print(f"Error: {e}")
        return None

def show_data(items, name, count):
    clear()
    print("=" * 50)
    print(f"   {name}")
    print("   By: Rashid Ali Mehar")
    print("=" * 50)
    print(f"\nRefresh #{count}  |  {datetime.now().strftime('%I:%M:%S %p')}\n")
    if not items:
        print("Koi video nahi mili.")
        return
    print(f"{'#':<3}{'Title':<40}{'Views'}")
    print("-" * 60)
    for i, item in enumerate(items[:5], 1):
        t = item["snippet"]["title"]
        v = int(item["statistics"].get("viewCount", 0))
        if len(t) > 37:
            t = t[:34] + "..."
        vs = f"{v/1000000:.1f}M" if v >= 1000000 else (f"{v/1000:.0f}K" if v >= 1000 else str(v))
        print(f"{i:<3}{t:<40}{vs}")
    print("\n" + "=" * 60)
    print("Agla refresh 60 sec mein... (CTRL+C = menu)")

def run_cat(key):
    cat = CATEGORIES[key]
    count = 0
    while True:
        count += 1
        items = search_yt(cat["query"])
        if items is not None:
            show_data(items, cat["name"], count)
        try:
            time.sleep(60)
        except KeyboardInterrupt:
            return

def main():
    while True:
        show_menu()
        choice = input("Apna option (0-8): ").strip()
        if choice == "0":
            print("Bye!")
            break
        if choice in CATEGORIES:
            try:
                run_cat(choice)
            except KeyboardInterrupt:
                pass
        else:
            print("Galat option!")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
