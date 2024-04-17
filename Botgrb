import telegram
import subprocess
from telegram.ext import CommandHandler, Updater

# Fungsi untuk menangani perintah /start
def start(update, context):
    update.message.reply_text('Halo! Kirim /reboot untuk me-reboot VPS.')

# Fungsi untuk menangani perintah /reboot
def reboot_sg1(update, context):
    # Menjalankan perintah reboot VPS
    subprocess.Popen(['sudo', 'reboot'])
    update.message.reply_text('VPS sedang di-reboot...')

def main():
    # Inisialisasi bot dengan token
    updater = Updater("6474341901:AAFlu-jiIXzz_4nESufZ7E1ZkkSkJTYkoNg", use_context=True)

    # Menambahkan handler perintah /start
    updater.dispatcher.add_handler(CommandHandler('start', start))

    # Menambahkan handler perintah /reboot
    updater.dispatcher.add_handler(CommandHandler('reboot_sg1', reboot_sg1))

    # Memulai bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
