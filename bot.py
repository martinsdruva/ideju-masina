import os
from openai import OpenAI
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Tu esi latviski runājošs TikTok satura eksperts ar milzīgu pieredzi virālā satura radīšanā. Sniedz konkrētus, īsus un praktiskus padomus latviešu valodā. Tava atbilde vienmēr ir noderīga, draudzīga un orientēta uz rezultātu."},
            {"role": "user", "content": user_input}
        ]
    )
    await update.message.reply_text(response.choices[0].message.content)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
