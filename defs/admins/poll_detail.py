import app_logger as loger
from aiogram.types import CallbackQuery
from defs.classes import User, Poll
from aiogram.utils import markdown as fmt
from database.admin_queryes import get_survey, my_users
from keyboards.inline.admin import PollDetails



log = loger.get_logger(__name__)


async def poll_detail(cb: CallbackQuery, callback_data: dict):
    u = User(cb.from_user)
    log.info(f"нажата кнопка деталей по опросу {callback_data['name']}")
    surv = get_survey(callback_data['id'])
    await cb.bot.delete_message(chat_id=u.id, message_id=cb.message.message_id)
    await cb.bot.send_message(chat_id=u.id,
                              text=fmt.text(
                                  fmt.text(f"Опрос {callback_data['name']}"),
                                  fmt.text(f"Количество вопросов {len(surv)}"),
                                  sep='\n'),
                              reply_markup=PollDetails().create_cb(poll_id=callback_data['id']))


async def poll_action(cb: CallbackQuery, callback_data: dict):
    u = User(cb.from_user)
    log.info(f"нажата кнопка действия по запросу {callback_data['id']}")
    await cb.bot.delete_message(chat_id=u.id, message_id=cb.message.message_id)
    if callback_data['action'] == 'sent_to_users':
        tests = read_poll(callback_data['id'])
        send_poll(tests, admin=u)


def read_poll(id: int):
    log.info(f'нажата кнопка отправка опроса {id}')
    surv = get_survey(id)
    tests = []
    for t in surv:
        p = Poll(question=t.question,
                 options=[x.text for x in t.options],
                 correct_option_id=t.correct_option_id)
        tests.append(p)
    return tests

def send_poll(tests: list, admin):
    log.info(f'отправка опросов')
    users = my_users(admin)
    print(users)
