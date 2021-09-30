import os

active_key = os.getenv('active_key')
username = os.getenv('username')
telegram_token = os.getenv('telegram_token')

from Adafruit_IO import Client
aio = Client('Username','Active Key')

from telegram.ext import Updater, MessageHandler, Filters

def demo1(bot,update):
  aio.send('light',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light is turned ON')

  def demo2(bot,update):
  aio.send('light',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light is turned OFF')

  def demo3(bot,update):
  aio.send('fan',1)
  chat_id = bot.message.chat_id
  bot.message.reply_text('fan is turned ON')

  def demo4(bot,update):
  aio.send('fan',0)
  chat_id = bot.message.chat_id
  bot.message.reply_text('fan is turned OFF')

def main(bot,update):
  a= bot.message.text
  if a =="Turn on the light":
    demo1(bot,update)
  elif a =="Turn off the light":
    demo2(bot,update)
  elif a =="Turn on the fan":
    demo3(bot,update)
  elif a =="Turn off the fan":
    demo4(bot,update)

bot_token = 'telegram_token'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()

