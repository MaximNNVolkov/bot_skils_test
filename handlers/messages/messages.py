from aiogram import Dispatcher
from defs.messages.messages import other_msg


def register_msg(dp: Dispatcher):
    dp.register_message_handler(other_msg)
