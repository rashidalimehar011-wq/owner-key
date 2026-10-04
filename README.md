# 📊 Social Media Trend Analyzer

**By: Rashid Ali Mehar**

Ek AI-powered tool jo **real-time social media trends** analyze karta hai — Google aur YouTube se live data fetch karke batata hai ke **aaj kya trend kar raha hai**.

---

## 🎯 Ye Tool Kya Karta Hai?

Ye tool 3 tarah ke trends analyze karta hai:

| File | Kya Karta Hai |
|------|---------------|
| `yt_live.py` | **YouTube** ke live trending videos (Pakistan) |
| `livetrend.py` | **Google Search** ke live trending topics (Pakistan) |
| `trendai.py` | **Demo** analysis (offline, bina internet) |
| `main.py` | Owner verification system (password protected) |

---

## 🚀 Install Kaise Karein?

```bash
# 1. Repo clone karo
git clone https://github.com/rashidalimehar011-wq/owner-key.git
cd owner-key

# 2. Required libraries install karo
pip install requests

# 3. Tool chalao
python yt_live.py
python yt_live.py
python livetrend.py
python trendai.py
cd ~/owner-key
cat > approval.py << 'ENDOFFILE'
#!/usr/bin/env python3
# ═══════════════════════════════════════════
#     👑  OWNER APPROVAL SYSTEM  👑
#     By: Rashid Ali Mehar
# ═══════════════════════════════════════════

import sys

# ⚠️ YAHAN APNA PASSWORD DAALO
OWNER_KEY = "Rashid@2024"

BANNER = """
╔═══════════════════════════════════════════╗
║   👑  OWNER APPROVAL REQUIRED  👑         ║
║   By: Rashid Ali Mehar                    ║
╚═══════════════════════════════════════════╝
"""

def verify_owner():
    print(BANNER)
    print("🔐 Ye tool sirf Owner ke liye hai.")
    print("")
    
    entered = input("Enter Owner Key: ").strip()
    
    if entered != OWNER_KEY:
        print("")
        print("❌ Access Denied!")
        print("   Ye tool sirf Rashid Ali Mehar use kar sakte hain.")
        print("")
        sys.exit(1)
    
    print("")
    print("✅ Welcome, Owner! 👑")
    print("► Tool start ho raha hai...")
    print("")
