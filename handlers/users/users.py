from fsm import StateUser
from aiogram import Dispatcher
from defs import change_values
from keyboards.inline import UserProducts


cb_change_prod = UserProducts()


def register_user(dp: Dispatcher):
    dp.register_callback_query_handler(change_values, cb_change_prod.cb.filter(), state=StateUser.change_sales)
