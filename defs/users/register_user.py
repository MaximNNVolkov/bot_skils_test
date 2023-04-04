import app_logger as log
from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from aiogram.utils import markdown as fmt
from defs.classes import User
from fsm.users import RegistrationUser
import re
from database.user_queryes import add_register_user


log = log.get_logger(__name__)


async def start_registration(message: Message, state: FSMContext):
    user = User(message.from_user)
    log.info('start registration, пользователь: '.format(user.info_user()))
    await state.set_state(RegistrationUser.enter_department)
    await message.bot.delete_message(chat_id=user.id, message_id=message.message_id)
    await message.answer(text=fmt.text(
        fmt.text(user.get_url(), ',', sep=''),
        fmt.text('Введите номер своего подразделения.'),
        fmt.text('Номер должен соответствовать шаблону: 0000/0000'),
        sep='\n'))


async def change_department(message: Message, state: FSMContext):
    user = User(message.from_user)
    log.info('change_department, пользователь: '.format(user.info_user()))
    mask = re.compile(r'\d\d\d\d/\d\d\d\d')
    text = message.text.strip()
    await message.bot.delete_message(chat_id=user.id, message_id=message.message_id-1)
    await message.bot.delete_message(chat_id=user.id, message_id=message.message_id)
    if mask.search(text):
        log.info('введенный текст соответствует маске {}'.format(text))
        await state.set_state(RegistrationUser.enter_name)
        await message.answer(text=fmt.text(
            fmt.text('Отлично!'),
            fmt.text('Введите Ваше имя.'),
            fmt.text('Имя необходимо указать кирилицей.'),
            sep='\n'))
        await state.set_data(data={'name': text})
    else:
        log.info('введенный текст НЕ соответствует маске {}'.format(text))
        await message.answer(text=fmt.text(
            fmt.text(user.get_url(), ',', sep=''),
            fmt.text('Подразделение указано некорректно.'),
            fmt.text('Номер должен соответствовать шаблону: 0000/0000'),
            sep='\n'))


async def change_name(message: Message, state: FSMContext):
    user = User(message.from_user)
    log.info('change_name, пользователь: '.format(user.info_user()))
    mask = re.compile(r'^[А-Яа-я][А-Яа-я]+$')
    text = message.text.strip()
    await message.bot.delete_message(chat_id=user.id, message_id=message.message_id-1)
    await message.bot.delete_message(chat_id=user.id, message_id=message.message_id)
    if mask.search(text):
        log.info('введенный текст соответствует маске {}'.format(text))
        await state.set_state(RegistrationUser.enter_s_name)
        await message.answer(text=fmt.text(
            fmt.text('Хорошо, ', text.title(), '.'),
            fmt.text('Введите первую букву Вашего отчества.'),
            fmt.text('Укажите только одну букву, кирилицей.'),
            sep='\n'))
        d = await state.get_data()
        d['n'] = text.title()
        await state.set_data(data=d)
    else:
        log.info('введенный текст НЕ соответствует маске {}'.format(text))
        await message.answer(text=fmt.text(
            fmt.text(user.get_url(), ',', sep=''),
            fmt.text('Имя необходимо указать кирилицей.'),
            sep='\n'))


async def change_s_name(message: Message, state: FSMContext):
    user = User(message.from_user)
    log.info('change_s_name, пользователь: '.format(user.info_user()))
    mask = re.compile(r'^[А-Яа-я]$')
    text = message.text.strip()
    await message.bot.delete_message(chat_id=user.id, message_id=message.message_id-1)
    await message.bot.delete_message(chat_id=user.id, message_id=message.message_id)
    if mask.search(text):
        log.info('введенный текст соответствует маске {}'.format(text))
        await state.set_state(RegistrationUser.enter_l_name)
        await message.answer(text=fmt.text(
            fmt.text('Хорошо.'),
            fmt.text('Введите первую букву Вашей фамилии.'),
            fmt.text('Укажите только одну букву, кирилицей.'),
            sep='\n'))
        d = await state.get_data()
        d['s'] = text.title()
        await state.set_data(data=d)
    else:
        log.info('введенный текст НЕ соответствует маске {}'.format(text))
        await message.answer(text=fmt.text(
            fmt.text(user.get_url(), ',', sep=''),
            fmt.text('Укажите только одну букву, кирилицей.'),
            sep='\n'))


async def change_l_name(message: Message, state: FSMContext):
    user = User(message.from_user)
    log.info('change_s_name, пользователь: '.format(user.info_user()))
    mask = re.compile(r'^[А-Яа-я]$')
    text = message.text.strip()
    await message.bot.delete_message(chat_id=user.id, message_id=message.message_id-1)
    await message.bot.delete_message(chat_id=user.id, message_id=message.message_id)
    if mask.search(text):
        log.info('введенный текст соответствует маске {}'.format(text))
        await state.set_state(RegistrationUser.enter_l_name)
        await message.answer(text=fmt.text(
            fmt.text('Хорошо.'),
            fmt.text('Вы успешно прошли регистрацию.'),
            fmt.text('Ожидайте начала тестирования.'),
            sep='\n'))
        d = await state.get_data()
        d['l'] = text.title()
        add_register_user(user, d)
    else:
        log.info('введенный текст НЕ соответствует маске {}'.format(text))
        await message.answer(text=fmt.text(
            fmt.text(user.get_url(), ',', sep=''),
            fmt.text('Укажите только одну букву, кирилицей.'),
            sep='\n'))
