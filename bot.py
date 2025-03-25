import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

TOKEN = "7862218443:AAH8t0nFsHGHvKB8P35JLkQZl2mrWV7htt4"  # 🔹 உன் New Token இங்கே Paste பண்ணு

# ✅ 12 ராசிகள் & பலன் (மறுவமுறையும் Random ஆக)
rasi_predictions = {
    "மேஷம்": ["இன்று உங்கள் முயற்சிகள் வெற்றி அடையும்.", "புதிய வாய்ப்புகள் கிடைக்கும்.", "தன்னம்பிக்கையுடன் செயல்படுங்கள்!"],
    "ரிஷபம்": ["உங்கள் செலவுகளை கவனமாக நிர்வகிக்கவும்.", "நேரத்தை சரியாக பயன்படுத்து.", "முடிவெடுக்கும் முன்பு யோசிக்கவும்."],
    "மிதுனம்": ["நண்பர்களால் உதவி கிடைக்கும்.", "குடும்பத்தில் சந்தோஷம் பெருகும்.", "புதிய தொழில்முனைவோர்களுக்கு நல்ல நாள்."],
    "கடகம்": ["உடல்நலத்தில் சிறிது கவனம் தேவை.", "மனதளவில் அமைதி பெற யோகாசனம் பயிலவும்.", "அதிர்ஷ்டம் உங்கள் பக்கம் இருக்கும்."],
    "சிம்மம்": ["உழைப்பிற்கு அங்கீகாரம் கிடைக்கும்.", "அதிர்ஷ்டமான நாள்!", "உங்கள் முயற்சிகளை தொடருங்கள்."],
    "கன்னி": ["தன்னம்பிக்கையுடன் செயல்படுங்கள்.", "புதிய தொழில் வாய்ப்பு கிடைக்கும்.", "நண்பர்கள் உதவுவார்கள்."],
    "துலாம்": ["நேர்மையாக செயல்படுங்கள்.", "உங்கள் முயற்சிகள் வெற்றி பெறும்.", "முழுமையாக திட்டமிட்டு செயல்படுங்கள்."],
    "விருச்சிகம்": ["சிறிய சிக்கல்கள் இருக்கும்.", "அதிக கோபம் வேண்டாம்.", "மனச்சோர்வு வராமல் இருக்க சிறிய இடைவெளி எடுக்கவும்."],
    "தனுசு": ["புதிய அனுபவங்கள் கிடைக்கும்.", "தகவல்களை பகிர்ந்து கொள்ள நல்ல நாள்.", "செயல்களை திட்டமிட்டு செய்யவும்."],
    "மகரம்": ["திடமான முடிவுகள் எடுக்க வேண்டிய நாள்.", "பணவசதி அதிகரிக்கும்.", "நல்ல செய்தி வரும்."],
    "கும்பம்": ["உடல்நலம் மேம்படும்.", "உடல் ஆரோக்கியத்திற்கு நல்ல நாள்.", "புதிய திட்டங்கள் வெற்றி பெறும்."],
    "மீனம்": ["புதிய நட்புகள் உருவாகும்.", "பணவரவு உண்டு.", "உங்கள் முயற்சிகள் வெற்றி பெறும்."]
}

# ✅ /start Command Function
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("வணக்கம்! 😊 உங்கள் ராசி பெயரை (தமிழில்) Type செய்யுங்கள், நான் பலனை சொல்கிறேன்!")

# ✅ ராசி பெயரை வைத்து RANDOM பலன் கூறும் Function
async def rasi_prediction(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text.strip()

    if user_text in rasi_predictions:
        prediction = random.choice(rasi_predictions[user_text])  # 🔥 Always Random Response
        await update.message.reply_text(f"🔮 **{user_text} பலன்:** {prediction}")
    else:
        await update.message.reply_text("⚠️ தயவுசெய்து சரியான ராசி பெயரை தமிழில் உள்ளிடவும்! (Ex: மேஷம், ரிஷபம், மிதுனம்...)")

def main():
    app = Application.builder().token(TOKEN).build()

    # ✅ Command Handlers
    app.add_handler(CommandHandler("start", start))  # /start command Handle
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, rasi_prediction))  # User Message Handle

    print("✅ Astrology Bot Running...")

    # Bot Polling Start
    app.run_polling()

if __name__ == "__main__":
    main()
