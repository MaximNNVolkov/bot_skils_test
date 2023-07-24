import app_logger as loger
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext
from defs.classes import User
from aiogram.utils import markdown as fmt
from database.admin_queryes import get_survey


log = loger.get_logger(__name__)


async def poll_detail(cb: CallbackQuery, callback_data: dict, state: FSMContext):
    u = User(cb.from_user)
    log.info(f"нажата кнопка деталей по опросу {callback_data['name']}")
    surv = get_survey(callback_data['id'])
    await cb.bot.delete_message(chat_id=u.id, message_id=cb.message.message_id)
    await cb.bot.send_message(chat_id=u.id, text=fmt.text(
        fmt.text(f"Опрос {callback_data['name']}"),
        fmt.text(f"Количество вопросов {len(surv)}"),
        sep='\n'
    ))
