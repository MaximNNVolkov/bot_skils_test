from aiogram import types
from aiogram.utils.callback_data import CallbackData


class PollMenu:

    def create(self):
        poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        poll_keyboard.add(types.KeyboardButton(text="Добавить вопрос",
                                               callback_data='AdminAddTest',
                                               request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
        poll_keyboard.add(types.KeyboardButton(text="Завершить создание тестирования",
                                               callback_data='AdminTestComplete'))
        return poll_keyboard


class MyPolls():

    def __init__(self):
        self.cb = CallbackData('mypolls', 'id', 'name')

    def show_polls(self, polls: dict):
        my_polls_cb = types.InlineKeyboardMarkup()
        my_polls_cb.row_width = len(polls)
        for b in polls:
            btn = types.InlineKeyboardButton(text=b['name'], callback_data=self.cb.new(id=b['id'], name=b['name']))
            my_polls_cb.row(btn)
        return my_polls_cb
