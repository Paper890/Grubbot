import paramiko
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
# Daftar informasi SSH untuk setiap VPS
vps_list = [
    {
        'name': 'sg1',
        'SSH_HOST': '152.42.235.204',
        'SSH_PORT': 22,
        'SSH_USERNAME': 'root',
        'SSH_PASSWORD': '#1Sanstr//1999'
    },
    {
        'name': 's1',
        'SSH_HOST': '152.42.218.78',
        'SSH_PORT': 22,
        'SSH_USERNAME': 'root',
        'SSH_PASSWORD': '@99Sandi'
    },
    {
        'name': 's2',
        'SSH_HOST': '139.59.108.116',
        'SSH_PORT': 22,
        'SSH_USERNAME': 'root',
        'SSH_PASSWORD': '@99Sandi'
    },
    {
        'name': 's3',
        'SSH_HOST': '157.230.44.162',
        'SSH_PORT': 22,
        'SSH_USERNAME': 'root',
        'SSH_PASSWORD': '@99Sandi'
    },
    {
        'name': 's4',
        'SSH_HOST': '128.199.164.52',
        'SSH_PORT': 22,
        'SSH_USERNAME': 'root',
        'SSH_PASSWORD': '@99Sandi'
    },
    # Tambahkan informasi SSH untuk VPS lain di sini
]
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Halo! Kirim /reboot <nama_vps> untuk me-reboot VPS.')
def reboot(update: Update, context: CallbackContext) -> None:
    vps_name = context.args[0]
    vps_info = next((vps for vps in vps_list if vps['name'].lower() == vps_name.lower()), None)
    if vps_info:
        if reboot_remote_vps(vps_info):
            update.message.reply_text(f"{vps_info['name']} sedang me-reboot...")
        else:
            update.message.reply_text(f"Gagal melakukan reboot {vps_info['name']}.")
    else:
        update.message.reply_text("VPS tidak ditemukan.")
def reboot_remote_vps(vps_info):
    try:
        # Membuat koneksi SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=vps_info['SSH_HOST'], port=vps_info['SSH_PORT'],
                           username=vps_info['SSH_USERNAME'], password=vps_info['SSH_PASSWORD'])
        # Menjalankan perintah reboot pada VPS
        stdin, stdout, stderr = ssh_client.exec_command('sudo reboot')
        print(stdout.read().decode('utf-8'))
        print(stderr.read().decode('utf-8'))
        # Menutup koneksi SSH
        ssh_client.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
def main():
    updater = Updater("6474341901:AAH574AEKvhq1jK_N0NMBLjGezFbXDQLm-s", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("reboot", reboot, pass_args=True))
    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
