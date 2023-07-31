from aiogram import types
from aiogram.utils.callback_data import CallbackData


class PollMenu:

    @staticmethod
    def create():
        poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        poll_keyboard.add(types.KeyboardButton(text="Добавить вопрос",
                                               callback_data='AdminAddTest',
                                               request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
        poll_keyboard.add(types.KeyboardButton(text="Завершить создание тестирования",
                                               callback_data='AdminTestComplete'))
        return poll_keyboard


class MyPolls:

    def __init__(self):
        self.cb = CallbackData('mypolls', 'id', 'name')

    def show_polls(self, polls: dict):
        my_polls_cb = types.InlineKeyboardMarkup()
        my_polls_cb.row_width = len(polls)
        for b in polls:
            btn = types.InlineKeyboardButton(text=b['name'], callback_data=self.cb.new(id=b['id'], name=b['name']))
            my_polls_cb.row(btn)
        return my_polls_cb


class PollDetails:

    def __init__(self):
        self.cb = CallbackData('poll_details', 'id', 'action')

    def create_cb(self, poll_id):
        poll_detail = types.InlineKeyboardMarkup()
        poll_detail.row_width = 2
        poll_detail.row(types.InlineKeyboardButton(text='Отправить всем пользователям',
                                                   callback_data=self.cb.new(id=poll_id,
                                                                             action='sent_to_users')))
        poll_detail.row(types.InlineKeyboardButton(text='Показать все вопросы теста',
                                                   callback_data=self.cb.new(id=poll_id,
                                                                             action='show_tests')))
        return poll_detail
