import app_logger as loger
from aiogram import types
from aiogram.utils import markdown as fmt
from defs.classes import User
from aiogram.utils.deep_linking import get_start_link
from database.admin_queryes import my_survives
from keyboards.inline.admin import MyPolls


log = loger.get_logger(__name__)


async def admin_gen_ref(message: types.Message):
    u = User(message.from_user)
    log.info('Кнопка admin_gen_ref, {}'.format(u.info_user()))
    link = await get_start_link(str(u.username), encode=True)
    await message.bot.send_message(chat_id=u.id, text=f"Для приглашения пользователей перешлите им следующее "
                                                      f"сообщение")
    await message.bot.send_message(chat_id=u.id, text=fmt.text(
        fmt.text('Добрый день!'),
        fmt.text('Присоединяйтесь к нашей группе тестирования'),
        fmt.hlink('присоединиться', link),
        sep='\n'))


async def admin_surveys_list(message: types.Message):
    u = User(message.from_user)
    log.info(f'Кнопка admin_surveys_list, {u.info_user()}')
    s = my_survives(u)
    await message.bot.send_message(chat_id=u.id, text=fmt.text('Список Ваших тестов'),
                                   reply_markup=MyPolls().show_polls(polls=s))

# TODO: Сделать реакцию на нажатие кнопки admin_surveys_list если нет созданных тестов
