from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import StateFilter


class FSMProcess(StatesGroup):
    USER_ID = State()
    WAITING_QUESTION = State()