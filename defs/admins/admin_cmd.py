import app_logger as loger
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils import markdown as fmt
from defs.classes import User


log = loger.get_logger(__name__)


async def admin_gen_ref(message: types.Message, state: FSMContext):
    u = User(message.from_user)
    log.info('Кнопка get_ref, {}'.format(u.info_user()))
    await message.bot.send_message(chat_id= u.id, text=f"Ваша реф. ссылка {link}")


