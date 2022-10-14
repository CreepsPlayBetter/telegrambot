# Имя бота: Ainur203819Bot
# Токен бота: 5730717754:AAEpmPXWWE7uzAX2SZwICGtA-D74eFKgPak
# Используем библиотеку: pyTelegramBotAPI

import telebot
from telebot import types

token = "5730717754:AAEpmPXWWE7uzAX2SZwICGtA-D74eFKgPak"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):  
    bot.send_message(message.chat.id,"Привет ✌️")


@bot.message_handler(commands=['sosi'])
def start_message(message):  
    bot.send_message(message.chat.id,"работает...")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    MyButton = types.KeyboardButton("Привет мир!")
    markup.add(MyButton)

bot.infinity_polling()


# @bot.message_handler(commands=['button'])
# def button_message(message):
#     # markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     MyButton = types.KeyboardButton("Привет мир!")
#     markup.add(MyButton)
    

bot.infinity_polling()
