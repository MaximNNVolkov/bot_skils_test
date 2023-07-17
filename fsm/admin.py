from aiogram.dispatcher.filters.state import State, StatesGroup


class CreateTest(StatesGroup):
    enter_name = State()
    enter_poll = State()
