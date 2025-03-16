import os
import sys

# Добавляем путь к папке с конфигурацией
sys.path.append(os.path.join(os.path.dirname(__file__), 'calories_data'))

import config
import telebot
from telebot import types
from db import get_user_data, clear_user_data, UserData, session
from commands import start, help, add, save_food, summary, reset, delete_food

bot = telebot.TeleBot(config.token)

bot.message_handler(commands=['start'])(lambda message: start.send_welcome(message, bot))
bot.message_handler(commands=['help'])(lambda message: help.send_help(message, bot))
bot.message_handler(commands=['add'])(lambda message: add.add_food(message, bot))
bot.message_handler(func=lambda message: ',' in message.text)(lambda message: save_food.save_food(message, bot))
bot.message_handler(commands=['summary'])(lambda message: summary.summary(message, bot))
bot.message_handler(commands=['reset'])(lambda message: reset.reset_data(message, bot))
bot.message_handler(commands=['delete'])(lambda message: delete_food.delete_food(message, bot))
bot.message_handler(func=lambda message: not message.text.startswith('/'))(lambda message: delete_food.delete_food_entry_handler(message, bot))

bot.polling()