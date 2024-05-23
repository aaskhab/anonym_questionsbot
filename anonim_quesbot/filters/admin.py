import logging

from aiogram import Bot
from aiogram.filters import BaseFilter
from aiogram.types import Message

from config import Config

async def check_sub(bot: Bot, channel_id: int, user_id: int) -> bool:
    try:
        user = await bot.get_chat_member(channel_id, user_id)
        return user.status != 'left'
    except Exception:
        return False