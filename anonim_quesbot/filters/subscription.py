from aiogram.filters import BaseFilter
from aiogram import Bot
from aiogram.types import Message


class CheckSubscription(BaseFilter):
    async def __call__(self, event: Message,  bot: Bot):
        sub = check_sub(bot, '@aaskhb', event.from_user.id)

        if sub:
            return True
        await event.answer('Ты не подписан на канал')
        return False
        

async def check_sub(bot: Bot, channel_id: int, user_id: int) -> bool:
    try:
        user = await bot.get_chat_member(channel_id, user_id)
        return user.status != 'left'
    except Exception:
        return False