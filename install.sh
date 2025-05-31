#!/bin/bash

echo "🔧 Predator Installer - Starting setup..."
sleep 1

# Check for root privileges
if [[ $EUID -ne 0 ]]; then
   echo "❌ Please run this script as root (use: sudo ./install.sh)"
   exit 1
fi

echo "📦 Updating system packages..."
apt update && apt upgrade -y

echo "🐍 Installing Python3 and pip..."
apt install -y python3 python3-pip

echo "🔌 Installing required system tools..."
apt install -y tor macchanger net-tools dnsutils iptables

echo "🧰 Installing Python dependencies from requirements.txt..."
pip3 install -r requirements.txt

echo "🛡️ Enabling required system modules..."
modprobe ip_tables
modprobe iptable_filter

echo "✅ Setup completed successfully!"
echo ""
echo "🚀 To launch Predator, run:"
echo "    python3 predator.py"
