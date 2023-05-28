from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


class UsersOkCancel:

    def create_kb():
        kb = InlineKeyboardMarkup()
        kb.row_width = 2
        btns = []
        btns.append(InlineKeyboardButton(text='OK', callback_data='UserOk'))
        btns.append(InlineKeyboardButton(text='Отмена', callback_data='UserCancel'))
        kb.row(btns[0], btns[1])
        return kb


class UsersMenu:

    def create_kb():
        kb = InlineKeyboardMarkup()
        kb.row_width = 2
        btns = []
        btns.append(InlineKeyboardButton(text='Регистрация', callback_data='UserReg'))
        btns.append(InlineKeyboardButton(text='Список тестов', callback_data='UserTestsList'))
        btns.append(InlineKeyboardButton(text='Пройденные тесты', callback_data='UserTestsComplete'))
        kb.row(btns[0], btns[1])
        kb.row(btns[2])
        return kb


class AdminsMenu:

    def create_kb():
        kb = InlineKeyboardMarkup()
        kb.row_width = 2
        btns = []
        btns.append(InlineKeyboardButton(text='Мои тесты', callback_data='AdminMyGroups'))
        btns.append(InlineKeyboardButton(text='Создать новый тест', callback_data='AdminNewGroups'))
        btns.append(InlineKeyboardButton(text='Пригласить пользователя', callback_data='AdminRefUser'))
        kb.row(btns[0], btns[1])
        kb.row(btns[2])
        return kb


class UserProducts():

    def __init__(self):
        self.cb = CallbackData('Change', 'product')

    def create_kb(self):
        btns = []
        kb = InlineKeyboardMarkup()
        kb.row_width = 3
        for k in self.my_d.keys():
            btns.append(InlineKeyboardButton(text=self.my_d[k],
                                             callback_data=self.cb.new(product=k)))
        kb.add(*btns)
        return kb
