import paramiko

# Informasi untuk masing-masing VPS
vps_info = {
    'vps1': {
        'ip': 'IP_VPS_1',
        'username': 'USERNAME_1',
        'password': 'PASSWORD_1'
    },
    'vps2': {
        'ip': 'IP_VPS_2',
        'username': 'USERNAME_2',
        'password': 'PASSWORD_2'
    },
    'vps3': {
        'ip': 'IP_VPS_3',
        'username': 'USERNAME_3',
        'password': 'PASSWORD_3'
    },
    'vps4': {
        'ip': 'IP_VPS_4',
        'username': 'USERNAME_4',
        'password': 'PASSWORD_4'
    }
}

# Fungsi untuk mereboot VPS menggunakan SSH
def reboot_vps(update, context):
    # Menerima argumen dari perintah
    args = context.args
    if len(args) != 1:
        context.bot.send_message(chat_id=update.effective_chat.id, text="Gunakan perintah /rebootvps [nama_vps]. Contoh: /rebootvps vps1")
        return

    vps_name = args[0]

    # Memeriksa apakah nama VPS yang diminta ada dalam daftar
    if vps_name not in vps_info:
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"VPS dengan nama {vps_name} tidak ditemukan.")
        return

    vps = vps_info[vps_name]

    try:
        # Buat koneksi SSH ke VPS
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=vps['ip'], port=22, username=vps['username'], password=vps['password'])

        # Kirim perintah reboot
        stdin, stdout, stderr = ssh_client.exec_command('sudo reboot')

        # Tunggu sampai perintah selesai dieksekusi
        stdout.channel.recv_exit_status()

        # Kirim pesan bahwa VPS sedang direboot
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"VPS {vps_name} sedang direboot.")

    except Exception as e:
        # Jika ada kesalahan, kirim pesan error
        context.bot.send_message(chat_id=update.effective_chat.id, text=f"Terjadi kesalahan saat mereboot VPS {vps_name}: {str(e)}")

    finally:
        # Tutup koneksi SSH
        ssh_client.close()

def main():
    # Token bot Telegram
    updater = Updater(token='{TOKEN}', use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Mendefinisikan handler perintah /start
    dp.add_handler(CommandHandler("start", start))

    # Mendefinisikan handler perintah /help
    dp.add_handler(CommandHandler("help", help))

    # Mendefinisikan handler perintah /rebootvps
    dp.add_handler(CommandHandler("rebootvps", reboot_vps))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
