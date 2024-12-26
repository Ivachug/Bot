# bot.py
import telebot
import os
import importlib
from config import TOKEN, ADMIN_ID
from db.db import init_db, add_user, get_user

bot = telebot.TeleBot(TOKEN)
init_db()

commands = {}

# Загрузка всех команд из папки hand
def load_commands():
    for filename in os.listdir('hand'):
        if filename.endswith('.py') and filename != 'command.py':  # Исключаем базовый класс
            module_name = filename[:-3]  # Убираем '.py'
            module = importlib.import_module(f'hand.{module_name}')
            command_class = getattr(module, f'{module_name.capitalize()}Command')
            commands[module_name] = command_class(bot)  # Передаем объект bot

load_commands()

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username
    chat_id = message.chat.id
    
    # Проверка и добавление пользователя в БД
    if not get_user(user_id):
        add_user(user_id, username, chat_id)

    # Вызываем команду "start"
    if 'start' in commands:
        commands['start'].execute(message)

@bot.message_handler(commands=['admin'])
def admin_panel(message):
    if 'admin' in commands:
        commands['admin'].execute(message)

@bot.message_handler(func=lambda message: message.text.lower() in commands)
def handle_command(message):
    command_key = message.text.lower()
    if command_key in commands:
        commands[command_key].execute(message)

bot.polling()

