from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from anonim_quesbot.filters.admin import AdminFilter
from anonim_quesbot.keyboards.admin import get_admin_kb
from anonim_quesbot.sql.db import get_stat

#📊📩

admin_router = Router()
admin_router.message.filter(AdminFilter())

@admin_router.message(Command('admin'))
async def user_mailing(message: Message):
     await message.answer('Вы вошли в админ-панель', reply_markup=get_admin_kb())

@admin_router.message(F.text == '📊Статистика')
async def get_bot_stat(message: Message):
     await message.answer(f'👤Всего пользователей: {get_stat()}')