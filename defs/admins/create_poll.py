import app_logger as loger
from aiogram.types import CallbackQuery, Message, ReplyKeyboardRemove
from aiogram.dispatcher import FSMContext
from aiogram.utils import markdown as fmt
from defs.classes import User, Poll
from database.user_queryes import admin_check
from database.admin_queryes import add_survey, test_add
from fsm.admin import CreateTest
from keyboards.inline.admin import PollMenu


log = loger.get_logger(__name__)


async def admin_create_new_test(cb: CallbackQuery, state: FSMContext):
    user = User(cb.from_user)
    log.info(f'нажата кнопка создать тест, пользователь: {user.info_user()}')
    u = admin_check(user=user)
    if u:
        await create_test_proc(cb.message, state)


async def create_test_proc(message: Message, state: FSMContext):
    user = User(message.from_user)
    log.info(f'начало процесса создания опроса: {user.info_user()}')
    await message.answer(text=fmt.text(
        fmt.text('Введите название тестирования'),
        sep='\n'),
        reply_markup=ReplyKeyboardRemove())
    await state.set_state(CreateTest.enter_name)


async def enter_poll(message: Message, state: FSMContext):
    user = User(message.from_user)
    log.info(f'пользователь ввел название опроса: {user.info_user()}')
    surv_id = add_survey(user, message.text)
    await state.set_data(data={'survey_id': surv_id, 'polls': []})
    await message.answer(text=fmt.text(
        fmt.text('Заполните вопрос'),
        sep='\n'),
        reply_markup=PollMenu().create())
    await state.set_state(CreateTest.enter_poll)


async def save_poll(message: Message, state: FSMContext):
    user = User(message.from_user)
    log.info(f'пользователь прислал опрос: {user.info_user()}')
    d = await state.get_data()
    poll = Poll(
        question=message.poll.question,
        options=[x.text for x in message.poll.options],
        correct_option_id=message.poll.correct_option_id,
    )
    d['polls'].append(poll)
    await state.set_data(data=d)


async def poll_complete(message: Message, state: FSMContext):
    user = User(message.from_user)
    log.info(f'пользователь pаершил добавление опросов: {user.info_user()}')
    await message.bot.delete_message(chat_id=user.id, message_id=message.message_id)
    await message.answer(text=fmt.text(
        fmt.text('Ваш опрос успешно сохранен'),
        fmt.text('все Ваши опросы вы можете найти в разделе Мои опросы'),
        sep='\n'),
        reply_markup=ReplyKeyboardRemove())
    d = await state.get_data()
    for poll in d['polls']:
        test_add(d['survey_id'], poll)
    await state.finish()
