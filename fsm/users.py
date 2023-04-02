import app_logger as logger
from aiogram.dispatcher.filters.state import State, StatesGroup


log = logger.get_logger(__name__)


class StateUser(StatesGroup):
    enter_id = State()
    enter_bch = State()
    enter_sup = State()
    enter_szdor = State()
    check_sales = State()
    change_sales = State()
    changed_sales = State()
