from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_inline_answer(user_id):
    button = [[InlineKeyboardButton(text='Ответить анонимно', callback_data=f'anonym_answer-{user_id}')]]

    keyboard = InlineKeyboardMarkup(inline_keyboard=button)

    return keyboard