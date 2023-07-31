import app_logger as loger
import asyncio
from aiogram import exceptions
from aiogram.types import Message


log = loger.get_logger(__name__)


async def send_message_to_users_handler(bot,
    user_id: int, text: str, disable_notification: bool = False
) -> bool:
    """
    Safe messages sender
    :param user_id:
    :param text:
    :param disable_notification:
    :return:
    """
    try:
        await bot.send_message(
            user_id,
            text,
            disable_notification=disable_notification
        )
    except exceptions.BotBlocked:
        log.error(f"Target [ID:{user_id}]: blocked by user")
    except exceptions.ChatNotFound:
        log.error(f"Target [ID:{user_id}]: invalid user ID")
    except exceptions.RetryAfter as e:
        log.error(
            f"Target [ID:{user_id}]: Flood limit is exceeded. "
            f"Sleep {e.timeout} seconds."
        )
        await asyncio.sleep(e.timeout)
        return await bot.send_message(user_id, text)  # Recursive call
    except exceptions.UserDeactivated:
        log.error(f"Target [ID:{user_id}]: user is deactivated")
    except exceptions.TelegramAPIError:
        log.exception(f"Target [ID:{user_id}]: failed")
    else:
        log.info(f"Target [ID:{user_id}]: success")
        return True
    return False


async def send_message_to_users(message: Message, text, users_list) -> int:
    """
    Simple broadcaster
    :return: Count of messages
    """
    count = 0
    bot = message.bot
    try:
        for user_id in users_list:
            if await send_message_to_users_handler(bot, user_id, text):
                count += 1
            # 20 messages per second (Limit: 30 messages per second)
            await asyncio.sleep(.05)
    finally:
        log.info(f"{count} messages successful sent.")

    return count
