import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters

BOT_TOKEN = os.getenv("7862218443:AAH8t0nFsHGHvKB8P35JLkQZl2mrWV7htt4")  # Render-ல் environment variable-ல் BOT_TOKEN set பண்ணணும்!

app = Flask(__name__)
bot = Bot(token=BOT_TOKEN)

# Function to handle "/start" command
def start(update, context):
    update.message.reply_text("👋 Welcome to Astrofun Bot!")

# Function to handle normal messages
def handle_message(update, context):
    text = update.message.text
    update.message.reply_text(f"🔮 Your query: {text}")

# Telegram Update Handler
dispatcher = Dispatcher(bot, None, use_context=True)
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

@app.route(f"/{BOT_TOKEN}", methods=["POST"])
def receive_update():
    update = Update.de_json(request.get_json(), bot)
    dispatcher.process_update(update)
    return "OK", 200

if __name__ == "__main__":
    WEBHOOK_URL = f"https://astrofun.onrender.com/{BOT_TOKEN}"
    bot.setWebhook(WEBHOOK_URL)
    app.run(host="0.0.0.0", port=5000)
