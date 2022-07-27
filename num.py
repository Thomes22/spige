import telebot
from telebot import TeleBot

bot_token = "5570483141:AAFdlXrpEdtKON9S5vG2jCeK6kYzTy7CR3c"

bot: TeleBot = telebot.TeleBot(token=bot_token, parse_mode=None)

@bot.message_handler(commands= ["/"]+ ["start"])
def sendmessages( message ):
    bot.send_message(message.chat.id ,"Type some thing to start")


@bot.message_handler(commands=["Hello"])
def sendmessages(message):
    bot.send_message(message.chat.id , "hi")

@bot.message_handler(commands=["hi"])
def sendmessages(message):
    bot.send_message(message.chat.id, "Hello")

@bot.message_handler(commands=["what is your name"])
def sendmessages(message):
    bot.send_message(message.chat.id, "IM cinifoks")

@bot.message_handler(commands=["whatsup"])
def sendmessages(message):
    bot.send_message(message.chat.id, "I'am doing grate thank you")




bot.polling()
