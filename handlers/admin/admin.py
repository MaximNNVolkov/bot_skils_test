from aiogram import types, Dispatcher
from defs.admins.admin_cmd import admin_gen_ref
from aiogram.dispatcher.filters.builtin import ChatTypeFilter, AdminFilter


def register_admin(dp: Dispatcher):
    dp.register_callback_query_handler(admin_gen_ref, text="AdminRefUser", state='*')
