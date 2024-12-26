from hand.command import Command
from config import CHANNEL_ID

class SendCommand(Command):
    def __init__(self, bot):
        self.bot = bot  # Сохраняем объект bot

    def execute(self, message):
        self.bot.send_message(message.chat.id, "Пожалуйста, прикрепите фото и дайте описание.")

    def handle_photo(self, photo_message):
        photo_id = photo_message.photo[-1].file_id
        description = photo_message.caption or "Без описания"
        self.bot.send_photo(CHANNEL_ID, photo_id, caption=description)

        self.bot.send_message(photo_message.chat.id, "Ваше сообщение размещено!")

    def get_keyboard(self):
        return get_main_keyboard()

