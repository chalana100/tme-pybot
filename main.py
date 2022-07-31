import os
import telebot


bot = telebot.Telebot("API key Here")
bot = telebot.TeleBot("5307911209:AAGrZplcySur71CEvQwYezA3dInCeCycvXs")


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hellow I'm chalana chamod")


@bot.message_handler(commands=["start"])   
def send_message(message):
    bot.send_message(message.chat.id, "https://www.fiverr.com/share/qeXrWd")
    

bot.polling()