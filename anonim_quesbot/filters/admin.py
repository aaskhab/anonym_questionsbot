import logging

from aiogram import Bot
from aiogram.filters import BaseFilter
from aiogram.types import Message

from config import load_config

class AdminFilter(BaseFilter):
    def __init__(self) -> None:
        config = load_config()
        self.admin_id = config.tg_bot.admin_ids
        logging.info('ADMIN_ID: %s', self.admin_id)
    
    async def __call__(self, message: Message) -> bool:
        return message.from_user.id == self.admin_id