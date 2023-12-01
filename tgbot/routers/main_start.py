# - *- coding: utf- 8 - *-
from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import Message

from tgbot.database.db_users import UserModel
from tgbot.keyboards.reply_main import menu_frep
from tgbot.utils.const_functions import ded
from tgbot.utils.misc.bot_models import FSM, ARS

router = Router(name=__name__)


# Открытие главного меню
@router.message(F.text.in_(('🔙 Main menu', '🔙 Return')))
@router.message(Command(commands=['start']))
async def main_start(message: Message, bot: Bot, state: FSM, arSession: ARS, User: UserModel):
    await state.clear()

    await message.answer(
        ded(f"""
            🔸 Hello, {User.user_name}
            🔸 Enter /start or /inline
        """),
        reply_markup=menu_frep(message.from_user.id),
    )
