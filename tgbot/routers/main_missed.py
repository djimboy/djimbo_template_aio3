# - *- coding: utf- 8 - *-
from aiogram import Router, Bot, F
from aiogram.types import CallbackQuery, Message

from tgbot.utils.const_functions import del_message
from tgbot.utils.misc.bot_models import FSM, RS

router = Router()


# Колбэк с удалением сообщения
@router.callback_query(F.data == 'close_this')
async def main_callback_close(call: CallbackQuery, bot: Bot, state: FSM, rSession: RS, my_user):
    await del_message(call.message)


# Колбэк с обработкой кнопки
@router.callback_query(F.data == '...')
async def main_callback_answer(call: CallbackQuery, bot: Bot, state: FSM, rSession: RS, my_user):
    await call.answer(cache_time=30)


# Колбэк с обработкой удаления сообщений потерявших стейт
@router.callback_query()
async def main_callback_missed(call: CallbackQuery, bot: Bot, state: FSM, rSession: RS, my_user):
    await call.answer(f"❗️ Miss callback: {call.data}", True)


# Обработка всех неизвестных команд
@router.message()
async def main_message_missed(message: Message, bot: Bot, state: FSM, rSession: RS, my_user):
    await message.answer(
        "♦️ Unknown command.\n"
        "♦️ Enter /start",
    )
