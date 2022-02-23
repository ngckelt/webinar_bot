from aiogram.dispatcher.filters.state import StatesGroup, State


class ConnectionWithManagerStates(StatesGroup):
    get_name = State()
    get_phone = State()

