from aiogram import types, Dispatcher
import app_logger as loger
from handlers import register_user, register_msg, register_admin, register_commands


log = loger.get_logger(__name__)


async def set_default(dp: Dispatcher):
    # создаем меню
    res = await dp.bot.set_my_commands([
        types.BotCommand("help", "Помощь"),
    ])
    log.debug('commands set result {}'.format(res))
    dp.bot.parse_mode = 'HTML'
    # регистрируем handlers
    register_commands(dp=dp)
    register_user(dp=dp)
    register_admin(dp=dp)
    register_msg(dp=dp)
