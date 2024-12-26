# hand/command.py
from abc import ABC, abstractmethod
from telebot import types

class Command(ABC):
    @abstractmethod
    def execute(self, message):
        pass

    @abstractmethod
    def get_keyboard(self):
        pass

