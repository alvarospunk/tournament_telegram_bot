# import telegram as tg
# import telegram.ext
# from telegram.ext import Updater, MessageHandler, CommandHandler, filters, CallbackContext
from telegram import Update, ForceReply, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = '710743623:AAEaG33UZd78fTEuZqRPIKmv8Dgn4C81-LM'
id_grupo_mora = '433115974'
id_alvaro = '11644706'

# Initialize the Updater and pass your bot token
updater = Updater(TOKEN, Updater.update_queue)
dispatcher = updater.dispatcher

# Define a function to send a response message
def respond_to_message(update, context):
    # Get the user's chat ID
    chat_id = update.message.chat_id

    print ("The user " + str(chat_id) + " is texting the bot.")

    # Send a response message
    context.bot.send_message(chat_id=chat_id, text="La mora ya sa escondio en su kueba")

def request_location(update, context):
    keyboard = KeyboardButton("Share your location", request_location=True)
    reply_markup = ReplyKeyboardMarkup([[keyboard]], resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text("To enable live location sharing, please share your location.", reply_markup=reply_markup)

def handle_location(update, context: CallbackContext):
    user = update.message.from_user
    location = update.message.location

    # Enable live location updates from the user
    context.bot.send_message(user.id, "You've enabled live location sharing with the bot. Your real-time location updates will be received.")
    context.bot.start_location_updates(user.id, location_received)

def location_received(bot, update):
    # Handle real-time location updates here
    user_id = update.effective_user.id
    location = update.message.location
    latitude = location.latitude
    longitude = location.longitude

    # Process and respond to location updates
    bot.send_message(user_id, f"Live location update received: Latitude {latitude}, Longitude {longitude}")

def location(update, context):
    chat_id = update.message.chat_id
    print ("The user " + str(chat_id) + " is texting the bot.")
    current_pos = (update.message.location.latitude,update.message.location.longitude)
    print(current_pos)
    context.bot.send_message(chat_id=chat_id, text=str(current_pos))

# Create a MessageHandler to trigger the function for all messages
# message_handler = MessageHandler(Filters.text & ~Filters.command, respond_to_message)
dispatcher.add_handler(CommandHandler("start", request_location))
dispatcher.add_handler(MessageHandler(filters.location, handle_location))

# Add the message handler to the dispatcher
# dispatcher.add_handler(message_handler)
# dispatcher.add_handler(MessageHandler(Filters.location, location))

def main():
    # Start the bot
    updater.start_polling()

    # Run the bot until Ctrl+C is pressed
    updater.idle()

if __name__ == '__main__':
    main()
