from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'fuck you {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'fuck you {update.effective_user.last_name}')


app = ApplicationBuilder().token("5307911209:AAHZwCKAfTU0sw1Ju6Oh8-Z9sbmAyVYP9p8").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))

app.run_polling()