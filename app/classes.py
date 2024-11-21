from aiogram.fsm.state import State, StatesGroup

class Company(StatesGroup):
    tg_id = State()