from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.filters import StateFilter


class FSMProcess(StatesGroup):
    USER_ID = State()
    WAITING_QUESTION = State()


class CreateMailing(StatesGroup):
    get_text = State()
    get_photo = State()
    get_keyboard_text = State()
    get_keyboard_url = State()
    confirm_sender = State()