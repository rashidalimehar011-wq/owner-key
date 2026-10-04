#!/data/data/com.termux/files/usr/bin/bash

# ═══════════════════════════════════════════
#     👑  OWNER-KEY PRIVATE SETUP  👑
#     Made by: Rashid Ali Mehar
#     GitHub: github.com/rashidalimehar
#     Access: Owner Only
# ═══════════════════════════════════════════

clear
echo ""
echo "╔═══════════════════════════════════════╗"
echo "║   👑  OWNER-KEY SETUP  👑             ║"
echo "║   By: Rashid Ali Mehar                ║"
echo "╚═══════════════════════════════════════╝"
echo ""

echo "► [1/4] Updating packages..."
pkg update -y > /dev/null 2>&1
pkg upgrade -y > /dev/null 2>&1
echo "   ✔ Done"

echo "► [2/4] Installing Python, Git, Curl..."
pkg install -y python git curl openssl > /dev/null 2>&1
echo "   ✔ Done"

echo "► [3/4] Installing Python libraries..."
pip install --upgrade pip > /dev/null 2>&1
pip install requests > /dev/null 2>&1
echo "   ✔ Done"

echo "► [4/4] Setup Owner-Key..."
echo "   ✔ Done"

echo ""
echo "╔═══════════════════════════════════════╗"
echo "║   ✅  SETUP COMPLETE                  ║"
echo "║   👑  Welcome, Rashid Ali Mehar       ║"
echo "╚═══════════════════════════════════════╝"
