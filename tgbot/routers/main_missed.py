# - *- coding: utf- 8 - *-
from aiogram import Router, Bot
from aiogram.filters import Text
from aiogram.types import CallbackQuery, Message

from tgbot.keyboards.reply_main import menu_frep
from tgbot.utils.misc.bot_models import FSM, AS

router = Router()


# Колбэк с удалением сообщения
@router.callback_query(Text(text="close_this"))
async def main_callback_close(call: CallbackQuery, bot: Bot, state: FSM, aSession: AS, my_user):
    await call.message.delete()


# Колбэк с обработкой кнопки
@router.callback_query(Text(text="..."))
async def main_callback_answer(call: CallbackQuery, bot: Bot, state: FSM, aSession: AS, my_user):
    await call.answer(cache_time=20)


# Колбэк с обработкой удаления сообщений потерявших стейт
@router.callback_query()
async def main_callback_missed(call: CallbackQuery, bot: Bot, state: FSM, aSession: AS, my_user):
    try:
        await call.message.delete()
    except:
        pass

    await call.message.answer("<b>❌ Данные не были найдены из-за перезапуска скрипта.\n"
                              "♻ Выполните действие заново.</b>",
                              reply_markup=menu_frep(call.from_user.id))


# Обработка всех неизвестных команд
@router.message()
async def main_message_missed(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await message.answer("♦ Неизвестная команда.\n"
                         "▶ Введите /start")
