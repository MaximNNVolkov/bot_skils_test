from fsm import RegistrationUser
from aiogram import Dispatcher
from defs.users import start_registration, change_department, change_name, change_s_name, change_l_name
from defs.users.change_polls import poll_change, poll_answer
from defs.users import registration_user


def register_user(dp: Dispatcher):
    dp.register_message_handler(start_registration, state=RegistrationUser.registration_start)
    dp.register_message_handler(change_department, state=RegistrationUser.enter_department)
    dp.register_message_handler(change_name, state=RegistrationUser.enter_name)
    dp.register_message_handler(change_s_name, state=RegistrationUser.enter_s_name)
    dp.register_message_handler(change_l_name, state=RegistrationUser.enter_l_name)
    dp.register_callback_query_handler(registration_user, text='UserReg', state='*')
    dp.register_callback_query_handler(poll_change, text='UserTestsList', state='*')
    dp.register_poll_answer_handler(poll_answer)
