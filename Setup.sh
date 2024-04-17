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
wget https://raw.githubusercontent.com/Paper890/crdrop/main/Do.py
# FOR DO CREATE
SERVER="$server"
sed -i "s/{SERVER}/$SERVER/g" Do.py

# fungsi running as system
cd
cd /etc/systemd/system
wget https://raw.githubusercontent.com/Paper890/crdrop/main/Do.service
sudo systemctl daemon-reload
sudo systemctl start Do
sudo systemctl enable Do
sudo systemctl restart Do


echo "Instalasi selesai."

cd
rm Setup.sh
