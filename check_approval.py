#!/usr/bin/env python3
# ═══════════════════════════════════════════
#     👑  OWNER APPROVAL CHECKER  👑
#     By: Rashid Ali Mehar
# ═══════════════════════════════════════════

import sys
import os

BANNER = """
╔═══════════════════════════════════════════╗
║   👑  OWNER APPROVAL REQUIRED  👑         ║
║   By: Rashid Ali Mehar                    ║
╚═══════════════════════════════════════════╝
"""

def load_keys():
    """Approved keys load karo"""
    keys = []
    key_file = os.path.join(os.path.dirname(__file__), "owner_keys.txt")
    
    try:
        with open(key_file, "r") as f:
            for line in f:
                line = line.strip()
                # Comment aur khali lines skip karo
                if line and not line.startswith("#"):
                    keys.append(line)
    except FileNotFoundError:
        print("⚠️  owner_keys.txt nahi mili!")
        return []
    
    return keys

def verify():
    """Check karo ke user approved hai ya nahi"""
    print(BANNER)
    print("🔐 Ye tool sirf approved users ke liye hai.")
    print("")
    
    entered = input("Enter Access Key: ").strip()
    
    keys = load_keys()
    
    if entered in keys:
        # Check karo owner hai ya guest
        if entered == "Rashid@2024":
            print("\n✅ Welcome, Owner! 👑")
        else:
            print(f"\n✅ Welcome! Access Granted.")
        print("► Tool start ho raha hai...\n")
        return True
    else:
        print("\n❌ Access Denied!")
        print("   Aap authorized nahi hain.")
        print("   Owner se contact karein: Rashid Ali Mehar")
        print("")
        sys.exit(1)

if __name__ == "__main__":
    verify()
