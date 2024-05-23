from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command('mailing'))
def user_mailing(message: Message, bot: Bot):
    bot.send_message()