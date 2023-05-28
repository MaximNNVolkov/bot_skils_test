from fsm import RegistrationUser
from aiogram import Dispatcher
from defs.users import change_department, change_name, change_s_name, change_l_name
from defs.users import start_registration


def register_user(dp: Dispatcher):
    dp.register_message_handler(change_department, state=RegistrationUser.enter_department)
    dp.register_message_handler(change_name, state=RegistrationUser.enter_name)
    dp.register_message_handler(change_s_name, state=RegistrationUser.enter_s_name)
    dp.register_message_handler(change_l_name, state=RegistrationUser.enter_l_name)
    dp.register_callback_query_handler(start_registration, text='UserReg', state='*')
