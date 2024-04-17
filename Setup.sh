#!/bin/bash

echo -e "MASUKKAN NAMA SERVER"
read -p "Masukkan Nama Server :" server

# Update paket repository
sudo apt update -y

# Upgrade paket yang sudah terinstal
sudo apt upgrade -y

# Instal Python 3 dan pip
sudo apt install python3 python3-pip -y

# Instal dependensi Python
pip install requests
pip install python-telegram-bot==12.0.0

mkdir -p grub/bot
# Pindah ke dalam folder yang baru dibuat
cd grub/bot
# Mengunduh skrip Python
wget https://raw.githubusercontent.com/Paper890/Grubbot/main/Botgrb.py
# FOR DO CREATE
SERVER="$server"
sed -i "s/{SERVER}/$SERVER/g" Botgrb.py

# fungsi running as system
cd
cd /etc/systemd/system
wget https://raw.githubusercontent.com/Paper890/Grubbot/main/Botgrb.service
sudo systemctl daemon-reload
sudo systemctl start Botgrb
sudo systemctl enable Botgrb
sudo systemctl restart Botgrb


echo "Instalasi selesai."

cd
rm Setup.sh
