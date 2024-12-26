# main/main_keyboard.py
from telebot import types

def get_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)  # Установка параметров
    keyboard.row(types.KeyboardButton("Разместить"), types.KeyboardButton("Личный кабинет"))  # Используем метод row
    keyboard.row(types.KeyboardButton("Обратная связь"), types.KeyboardButton("Помощь проекту"))  # Также в новом ряду
    return keyboard

