import app_logger as logger
from aiogram.dispatcher.filters.state import State, StatesGroup


log = logger.get_logger(__name__)


class RegistrationUser(StatesGroup):
    enter_department = State()
    enter_name = State()
    enter_l_name = State()
    enter_s_name = State()