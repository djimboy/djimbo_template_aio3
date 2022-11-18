# - *- coding: utf- 8 - *-
from aiogram import Router, Bot
from aiogram.filters import Text, Command
from aiogram.types import Message

from tgbot.keyboards.reply_main import menu_frep
from tgbot.utils.misc.bot_models import FSM, AS

router = Router()


# Открытие главного меню
@router.message(Text(text=['🔙 Главное меню']))
@router.message(Command(commands=['start']))
async def main_start(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await state.clear()

    await message.answer("🔸 Бот готов к использованию.\n"
                         "🔸 Если не появились вспомогательные кнопки\n"
                         "▶ Введите /start",
                         reply_markup=menu_frep(message.from_user.id))
