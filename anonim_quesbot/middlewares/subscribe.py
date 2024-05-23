from typing import Callable, Dict, Any, Awaitable

from aiogram import Bot
from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery
from anonim_quesbot.keyboard.check_sub import get_check_kb


class CheckSubscription(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: CallbackQuery,
            # bot: Bot,
            data: Dict[str, Any],
    ) -> Any:
        chat_member = await event.bot.get_chat_member("@aaskhb", event.from_user.id)

        if chat_member.status == 'left':
            await event.answer('Если хотите пользоваться ботом, подпишитесь на канал', reply_markup=get_check_kb())
        else:
            bot = Bot
            await bot.delete_message(chat_id=event.message.chat.id, message_id=event.message.message_id)
            return await handler(event, data)