import telebot 
import os
import telegram_send
import time




TOKEN = '5041192139:AAGlqZeqb58P-WI__MWaDVRk5XP0BzfgJWw'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(msg):
  bot.reply_to(msg, 'سلام حشری')

file = open("url.txt","r")
lines = file.readlines()

for i in lines:
  bot.send_photo(-332488397, i)
  time.sleep(60)

bot.polling()
