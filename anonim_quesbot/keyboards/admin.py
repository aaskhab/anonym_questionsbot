from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def get_admin_kb():
    stat_btn = KeyboardButton(text='📊Статистика')
    # mailing = KeyboardButton(text='📩Сделать рассылку')

    kb = [[stat_btn]]

    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    
    return keyboard

def get_mailing_kb():
    confirm_btn = KeyboardButton(text='Начать рассылку')
    cancel_btn = KeyboardButton(text='Отменить')

    kb = [[confirm_btn, cancel_btn]]

    keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

    return keyboard