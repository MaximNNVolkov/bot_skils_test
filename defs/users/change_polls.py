import app_logger as log
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.utils import markdown as fmt
from defs.classes import User


log = log.get_logger(__name__)


async def poll_change(cb: CallbackQuery, state: FSMContext):
    user = User(cb.from_user)
    log.info(f'нажата кнопка список тестов, пользователь: {user.info_user()}')
    pol = await cb.message.bot.send_poll(chat_id=user.id,
                                   question='вот мой первый вопрос',
                                   options=['1 variant', '2 variant', '3 variant', '4 variat'],
                                   type='regular',
                                   protect_content=True,
                                   is_anonymous=False
                                   )
    state.set_data(poll = pol.message_id)
    print(pol)


async def poll_answer(cb: CallbackQuery, state: FSMContext):
    user = User(cb.user)
    log.info(f'получен ответ на вопрос, опрос: {cb.poll_id}, '
             f'ответ {cb.option_ids}, от пользователя {user.info_user()}')
    cb.bot.delete_message(user.id, state.get_data())
