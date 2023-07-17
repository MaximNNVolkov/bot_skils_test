from aiogram import types


class PollMenu:

    def create():
        poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        poll_keyboard.add(types.KeyboardButton(text="Добавить вопрос",
                                               callback_data='AdminAddTest',
                                               request_poll=types.KeyboardButtonPollType(type=types.PollType.QUIZ)))
        poll_keyboard.add(types.KeyboardButton(text="Завершить создание тестирования",
                                               callback_data='AdminTestComplete'))
        return poll_keyboard
