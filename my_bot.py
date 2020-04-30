# coding=utf-8
import telebot
from telebot import types

TOKEN = '1032654775:AAGLEIdWAnDa7sYIgy345ev1GyYaJ-xbFOM'


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands = ['start'])
def startThisShit(message):
    startMenu = types.InlineKeyboardMarkup()
    buttonOne = types.InlineKeyboardButton(text='Пицца', callback_data='Pizza')
    buttonTwo = types.InlineKeyboardButton(text='Мясо', callback_data='Meat')
    startMenu.add(buttonOne, buttonTwo)
    bot.send_message(message.chat.id, 'Выберите товар', reply_markup=startMenu)

def mainMenuInline():
    mainMenu = types.InlineKeyboardMarkup()
    mainMenuButton = types.InlineKeyboardButton(text='Вернуться в главное меню', callback_data='main_menu')
    mainMenu.add(mainMenuButton)
    return mainMenu

def meatWeightInline():
    meatWeightMenu = types.InlineKeyboardMarkup()
    buttonMeatWeightMenu1 = types.InlineKeyboardButton(text='200 грамм', callback_data='weight_meat200')
    buttonMeatWeightMenu2 = types.InlineKeyboardButton(text='460 грамм', callback_data='weight_meat460')
    buttonMeatWeightMenu3 = types.InlineKeyboardButton(text='1000 грамм', callback_data='weight_meat1000')
    meatWeightMenu.add(buttonMeatWeightMenu1, buttonMeatWeightMenu2, buttonMeatWeightMenu3)
    return meatWeightMenu

def pizzaWeightInline():
    pizzaWeightMenu = types.InlineKeyboardMarkup()
    buttonPizzaWeightMenu1 = types.InlineKeyboardButton(text='300 грамм', callback_data='weight_pizza300')
    buttonPizzaWeightMenu2 = types.InlineKeyboardButton(text='400 грамм', callback_data='weight_pizza400')
    buttonPizzaWeightMenu3 = types.InlineKeyboardButton(text='500 грамм', callback_data='weight_pizza500')
    pizzaWeightMenu.add(buttonPizzaWeightMenu1, buttonPizzaWeightMenu2, buttonPizzaWeightMenu3)
    return pizzaWeightMenu

@bot.callback_query_handler(func=lambda c: True)
def putInline(c):
    if c.data == 'Pizza':
        bot.edit_message_text('Выберите вес пиццы', parse_mode="HTML", chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=pizzaWeightInline())
        return pizzaWeightInline()
    elif c.data == 'Meat':
        bot.edit_message_text('Выберите вес мяса', parse_mode="HTML", chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=meatWeightInline())
    elif c.data[:11] == 'weight_meat':
        bot.edit_message_text('Вы заказали ' + str(c.data[11:]) + ' грамм мяса', parse_mode="HTML", chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=mainMenuInline())
        bot.send_message(459531155, """Пользователь: @""" + str(c.message.chat.username) + """\r
        Заказал """ + str(c.data[11:]) + """ грамм мяса""", parse_mode="HTML")
    elif c.data[:12] == 'weight_pizza':
        bot.edit_message_text('Вы заказали ' + str(c.data[12:]) + ' грамм пиццы', parse_mode="HTML", chat_id=c.message.chat.id, message_id=c.message.message_id)
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=mainMenuInline())
        bot.send_message(459531155, """Пользователь: @""" + str(c.message.chat.username) + """\r
        Заказал """ + str(c.data[12:]) + """ грамм пиццы""", parse_mode="HTML")

bot.polling()