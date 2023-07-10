from aiogram import types
from aiogram.utils import markdown as fmt
from defs.classes import User
from aiogram.dispatcher import FSMContext
from keyboards import inline
from aiogram.utils.deep_linking import get_start_link
from database import add_admin
from database.user_queryes import add_user_group


async def cmd_start_proc(msg: types.Message, state: FSMContext):

    args = msg.get_args()
    user = User(msg.from_user)
    await cmd_process(args, msg, state, user)
    return user


async def __msg_user__(msg, state, user, args):
    await __clean_msg__(msg, state, )
    add_user_group(user.id, args)
    await msg.bot.send_message(chat_id=user.id,
                               text=fmt.text(fmt.text(user.get_url(), 'привет!', sep=', '),
                                             fmt.text("Я бот-экзаменатор."),
                                             sep='\n'),
                               reply_markup=inline.UsersMenu.create_kb())


async def __msg_admin__(msg, state, user):
    await __clean_msg__(msg, state, )
    link = await get_start_link(str(user.username), encode=True)
    code = link.split('start=')[-1]
    add_admin(user=user, ref_code=code)
    await msg.bot.send_message(chat_id=user.id,
                               text=fmt.text(fmt.text(user.get_url(), 'привет!', sep=', '),
                                             fmt.text("Я бот-экзаменатор."),
                                             sep='\n'),
                               reply_markup=inline.AdminsMenu.create_kb())


async def __clean_msg__(msg, state):
    await state.reset_state(with_data=True)
    await msg.bot.delete_message(chat_id=msg.from_user.id, message_id=msg.message_id)


async def cmd_process(args, msg, state, user):
    if args:
        await __msg_user__(msg, state, user, args)
    else:
        await __msg_admin__(msg, state, user)
