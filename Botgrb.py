import telegram
import subprocess
from telegram.ext import CommandHandler, Updater

# Fungsi untuk menangani perintah /reboot
def reboot_{SERVER}(update, context):
    # Menjalankan perintah reboot VPS
    subprocess.Popen(['sudo', 'reboot'])
    update.message.reply_text('VPS sedang di-reboot...')

def main():
    # Inisialisasi bot dengan token
    updater = Updater("6474341901:AAFlu-jiIXzz_4nESufZ7E1ZkkSkJTYkoNg", use_context=True)

    # Menambahkan handler perintah /reboot
    updater.dispatcher.add_handler(CommandHandler('reboot_{SERVER}', reboot_{SERVER}))

    # Memulai bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
