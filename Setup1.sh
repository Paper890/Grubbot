#!/bin/bash

mkdir -p grub/bot
# Pindah ke dalam folder yang baru dibuat
cd grub/bot
# Mengunduh skrip Python
wget https://raw.githubusercontent.com/Paper890/Grubbot/main/Botgrb.py
chmod +x Botgrb.py
# 
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
rm Setup1.sh
