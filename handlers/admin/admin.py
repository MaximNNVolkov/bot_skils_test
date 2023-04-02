from aiogram import types, Dispatcher
from defs.admins.admin_cmd import admin_cmd
from aiogram.dispatcher.filters.builtin import ChatTypeFilter, AdminFilter


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_cmd,
                                ChatTypeFilter(chat_type=types.ChatType.PRIVATE) and AdminFilter(),
                                commands="admin")
