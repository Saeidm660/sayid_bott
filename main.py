import telebot 
import os
import telegram_send
import time




TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
  bot.reply_to(msg, 'سلام حشری')

file = open("url.txt","r")
lines = file.readlines()

for i in lines:
  bot.send_photo(-1001208760301, i)
  time.sleep(60)

bot.polling()
