import app_logger as loger
from aiogram import types
from aiogram.utils import markdown as fmt
from defs.classes import User


log = loger.get_logger(__name__)


async def admin_cmd(message: types.Message):
    await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)
    u = User(message.from_user, message.chat.id)
    log.info(u.info_user())
    log.info('Запрос Admin. Пользователь {}, группа {}'.format(u.id, u.group))
    await message.bot.send_message(chat_id=u.user_id, text=fmt.text('Привет!'))
