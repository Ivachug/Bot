from hand.command import Command
from config import ADMIN_ID

class AdminCommand(Command):
    def __init__(self, bot):
        self.bot = bot  # Сохраняем объект bot

    def execute(self, message):
        if message.from_user.id == ADMIN_ID:
            markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            markup.add(telebot.types.KeyboardButton("Просмотр пользователей"))
            markup.add(telebot.types.KeyboardButton("Очистить базу данных"))
            self.bot.send_message(message.chat.id, "Вы в админ панели. Выберите действие:", reply_markup=markup)
        else:
            self.bot.send_message(message.chat.id, "У вас нет доступа к административной панели.")

    def get_keyboard(self):
        return telebot.types.ReplyKeyboardRemove()  # Убираем клавиатуру

