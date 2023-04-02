from comands import cmd_start, cmd_help, cmd_stop, cmd_register
from aiogram import Dispatcher


def register_commands(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands="start", state='*')
    dp.register_message_handler(cmd_help, commands="help", state='*')
    dp.register_message_handler(cmd_stop, commands="stop", state='*')
    dp.register_message_handler(cmd_register, commands="register", state='*')
