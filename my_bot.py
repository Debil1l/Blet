# coding=utf-8
import telebot
from telebot import types

TOKEN = '1032654775:AAGLEIdWAnDa7sYIgy345ev1GyYaJ-xbFOM'


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def startThisShit(message):
    startMenu = types.InlineKeyboardMarkup()
    buttonOne = types.InlineKeyboardButton(text='Пицца')
    buttonTwo = types.InlineKeyboardButton(text='Мясо')
    startMenu.add(buttonOne, buttonTwo)
    bot.send_message(message.chat.id, 'Выберите товар', reply_markup=startMenu)
bot.polling()
