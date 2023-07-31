from aiogram import types, Dispatcher
from defs.admins.admin_cmd import admin_gen_ref, admin_surveys_list
from defs.admins.create_poll import admin_create_new_test, enter_poll, save_poll, poll_complete
from defs.admins.poll_detail import poll_detail, poll_action
from keyboards.inline.admin import MyPolls, PollDetails
from fsm.admin import CreateTest


def register_admin(dp: Dispatcher):
    dp.register_message_handler(poll_complete, text='Завершить создание тестирования',
                                state=CreateTest.enter_poll)
    dp.register_callback_query_handler(admin_gen_ref, text="AdminRefUser", state='*')
    dp.register_callback_query_handler(admin_surveys_list, text='AdminMyTests', state='*')
    dp.register_callback_query_handler(admin_create_new_test, text='AdminNewTest', state='*')
    dp.register_message_handler(enter_poll, state=CreateTest.enter_name)
    dp.register_message_handler(save_poll, content_types=['poll'], state=CreateTest.enter_poll)
    dp.register_callback_query_handler(poll_detail, MyPolls().cb.filter())
    dp.register_callback_query_handler(poll_action, PollDetails().cb.filter())

