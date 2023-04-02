import app_logger as loger
from aiogram.utils import markdown as fmt
from defs.classes import User
from fsm import StateUser
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, CallbackQuery
from keyboards import inline


log = loger.get_logger(__name__)


def txt_false():
    return 'Вводи только цифры. Давай снова'


async def change_values(msg: Message, state: FSMContext):
    u = User(msg.from_user)
    log.info(' '.join([await state.get_state(), msg.text, u.info_user()]))
    d = await state.get_data()
    await state.set_state(StateUser.check_sales)
    await msg.answer(text=txt_false(u, await state.get_data()),
                         reply_markup=inline.UsersCheckSales.create_kb())
