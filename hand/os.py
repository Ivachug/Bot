# hand/os.py

from hand.command import Command
from main.main_keyboard import get_main_keyboard

class OSCommand(Command):
    def __init__(self, bot):
        self.bot = bot  # Сохраняем объект bot

    def execute(self, message):
        self.bot.send_message(message.chat.id, 
                              "Обратная связь отправлена! Мы свяжемся с вами в ближайшее время.", 
                              reply_markup=self.get_keyboard())

    def get_keyboard(self):
        return get_main_keyboard()

