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


class UserProducts():

    def __init__(self):
        # u = UserSales()
        self.my_d = {}#u.my_d
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
