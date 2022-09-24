# - *- coding: utf- 8 - *-
from aiogram import types, Router
from aiogram.types import CallbackQuery

from tgbot.keyboards.reply_main import menu_frep
from tgbot.utils.misc.bot_models import FSM

router = Router()


# Колбэк с удалением сообщения
@router.callback_query(text="close_this")
async def processing_callback_close(call: CallbackQuery, state: FSM):
    await call.message.delete()


# Колбэк с обработкой кнопки
@router.callback_query(text="...")
async def processing_callback_answer(call: CallbackQuery, state: FSM):
    await call.answer(cache_time=20)


# Колбэк с обработкой удаления сообщений потерявших стейт
@router.callback_query()
async def processing_callback_missed(call: CallbackQuery, state: FSM):
    try:
        await call.message.delete()
    except:
        pass

    await call.message.answer("<b>❌ Данные не были найдены из-за перезапуска скрипта.\n"
                              "♻ Выполните действие заново.</b>",
                              reply_markup=menu_frep(call.from_user.id))


# Обработка всех неизвестных команд
@router.message()
async def processing_message_missed(message: types.Message, state: FSM):
    await message.answer("♦ Неизвестная команда.\n"
                         "▶ Введите /start")
