from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "7624623108:AAHMZMmr58G6ze21Ow6bnOAdGIRqmS3uuTU"

def start(update: Update, context: CallbackContext):
    keyboard = [[KeyboardButton("Поділитися номером", request_contact=True)]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text("Будь ласка, поділіться вашим номером телефону:", reply_markup=reply_markup)

def contact_handler(update: Update, context: CallbackContext):
    contact = update.message.contact
    update.message.reply_text(f"Дякую! Ваш номер: {contact.phone_number}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.contact, contact_handler))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
