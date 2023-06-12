import app_logger as log
from defs.classes import User
from aiogram import types
from aiogram.utils import markdown as fmt
from aiogram.dispatcher import FSMContext
from keyboards import inline
from comands.сmd_start_proc import cmd_start_proc


log = log.get_logger(__name__)


async def cmd_start(message: types.Message, state: FSMContext):
    user = await cmd_start_proc(message, state)
    log.info(f'кнопка старт. {user.info_user()}')


async def cmd_help(message: types.Message, state: FSMContext):
    u = User(message.from_user)
    log.info('кнопка хэлп ' + u.info_user())
    await state.reset_state(with_data=True)
    await message.bot.delete_message(chat_id=u.id, message_id=message.message_id)
    await message.bot.send_message(chat_id=message.from_user.id, text=fmt.text(
            fmt.text(u.get_url(), ', ', sep=''),
            fmt.text('Напишите Ваш вопрос, перешлю его админимстратору.'),
            sep=''), reply_markup=inline.UsersOkCancel.create_kb())


async def cmd_stop(message: types.Message, state: FSMContext):
    u = User(message.from_user)
    log.info('бот остановлен ' + u.info_user())
    await state.reset_state(with_data=False)


async def bot_block_error(message: types.Message):
    await message.reply("Что то не так. Давай снова /start")
