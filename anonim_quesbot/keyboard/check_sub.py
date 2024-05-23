from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_check_kb():
    channel_btns = [[InlineKeyboardButton(text='Asĸнaв', url='https://t.me/aaskhb', callback_data='channel_pressed'),\
                      InlineKeyboardButton(text='✅ Подтвердить', callback_data='confirm_pressed')]]

    keyboard = InlineKeyboardMarkup(inline_keyboard=channel_btns)

    return keyboard