import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.enums import ParseMode

from anonim_quesbot.handlers import user_handler
from anonim_quesbot.middlewares.subscribe import CheckSubscription
from anonim_quesbot.filters.subscription import CheckSubscription
from config import load_config


logger = logging.getLogger(__name__)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s'
    )
    logger.info('Starting bot')
    
    config = load_config()
    bot = Bot(
              config.tg_bot.token,
              parse_mode=ParseMode.HTML)
    redis = Redis(host='localhost')
    storage = RedisStorage(redis=redis)
    
    dp = Dispatcher(storage=storage)
    # dp.message.middleware(CheckSubscription())
    dp.include_router(user_handler.user_router)
    logger.info('Подключаем роутеры')
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Бот был отключен')