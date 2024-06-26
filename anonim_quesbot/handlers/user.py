import logging

from aiogram import Router, Bot
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import F

from anonim_quesbot.sql.db import add_to_db, get_user, update_user
from anonim_quesbot.FSM.state import FSMProcess
from anonim_quesbot.keyboards.user import get_inline_answer
from anonim_quesbot.filters.subscription import CheckSubscription

user_router = Router()

@user_router.message(CommandStart())    #Роутер на команду start
async def start_command(message: Message, state: FSMContext):
    user_id = message.from_user.id
    
    if ' ' in message.text: # Условие для отлавливания id из ссылки
        partner = message.text.split()[1]
        
        try:
            logging.info('The partner id: %s', partner)
            partner = int(partner)

            if get_user(partner):
                pass
            else:
                await message.answer('Такой пользователь не найден')
                # return


            if user_id == partner:
                await message.answer('Вы не можете написать сами себе')
                logging.info('Пользователь пытается написать самому себе')
            
            else:
                await message.answer('Введите сообщение для отправки пользователю')
                await state.set_state(FSMProcess.USER_ID)
                await state.update_data(USER_ID = partner)

        except ValueError:
            pass
    else:
        if get_user(user_id):
            update_user(user_id, message.from_user.first_name, message.from_user.username)
        else:
            add_to_db(user_id, message.from_user.first_name, message.from_user.username)
        await message.answer('🔗<b>Твоя ссылка для вопросов:</b>\n'
                            f't.me/hattarlobot?start={user_id}\n\n\n'
                            'Поделись со своей ссылкой, чтобы люди смогли задать тебе анонимный вопрос!')
    
@user_router.message(FSMProcess.USER_ID, F.text)
async def get_answer(message: Message,  bot: Bot, state: FSMContext):
    user_id = message.from_user.id
    data = await state.get_data()
    partner_id = data.get('USER_ID')
    await bot.send_message(partner_id, text=f'<b>📩Получено новое сообщение:</b>\n\n{message.text}', reply_markup=get_inline_answer(user_id))
    await message.answer(f'<b>✅Ваше сообщение успешно отправлено</b>\n\n'
                         '🔗<b>Твоя ссылка для вопросов:</b>\n'
                            f't.me/hattarlobot?start={message.from_user.id}\n\n\n'
                            'Поделись со своей ссылкой, чтобы люди смогли задать тебе анонимный вопрос!')
    await state.clear()

@user_router.message(FSMProcess.USER_ID, ~F.text)
async def not_text(message: Message):
    await message.answer('Отправлять можно только текстовые сообщения')

@user_router.callback_query(F.data.startswith('anonym_answer-')) #Роутер на клавишу ответить
async def answer_callback(callback: CallbackQuery, state: FSMContext):
    user_id = int(callback.data.split('-')[1])
    await callback.answer()
    await callback.message.answer('<b>Введите ваш ответ на вопрос</b>')
    await state.update_data(USER_ID=user_id)
    await state.set_state(FSMProcess.WAITING_QUESTION)

@user_router.message(FSMProcess.WAITING_QUESTION, F.text)
async def answer_to_question(message: Message, state: FSMContext, bot: Bot):
    user_id = message.from_user.id
    data = await state.get_data()
    partner_id = data.get('USER_ID')
    
    await bot.send_message(partner_id, text=f'<b>📩Получено новое сообщение:</b>\n\n{message.text}',
                            reply_markup=get_inline_answer(user_id))
    await message.answer(f'<b>✅Ваше сообщение успешно отправлено</b>\n\n'
                         '🔗<b>Твоя ссылка для вопросов:</b>\n'
                            f't.me/hattarlobot?start={message.from_user.id}\n\n\n'
                            'Поделись со своей ссылкой, чтобы люди смогли задать тебе анонимный вопрос!')
    await state.clear()

@user_router.message(FSMProcess.WAITING_QUESTION, ~F.text)
async def not_wait_text(message: Message):
    await message.answer('Отправлять можно только текстовые сообщения')

@user_router.message()
async def other_answers(message: Message):
    await message.answer('Некорректное сообщение')