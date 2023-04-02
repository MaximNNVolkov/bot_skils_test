import app_logger as logger
from aiogram.dispatcher.filters.state import State, StatesGroup
log = logger.getLogger(__name__)


class Orders(StatesGroup):
    waiting_id = State()
    waiting_photo = State()
    waiting_geo = State()
