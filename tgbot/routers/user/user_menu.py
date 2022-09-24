# - *- coding: utf- 8 - *-
from aiogram import Router, Bot
from aiogram.types import Message

from tgbot.keyboards.inline_main import menu_finl
from tgbot.keyboards.inline_misc import user_inl
from tgbot.keyboards.reply_misc import user_rep
from tgbot.utils.misc.bot_models import FSM, AS

router = Router()


# Кнопка - User Inline
@router.message(text="User Inline")
async def user_button_inline(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await state.clear()

    await message.answer("Click Button - User Inline", reply_markup=user_inl)


# Кнопка - User Reply
@router.message(text="User Reply")
async def user_button_reply(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await state.clear()

    await message.answer("Click Button - User Reply", reply_markup=user_rep)


# Команда - /inline
@router.message(commands="inline")
async def user_command_inline(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await state.clear()

    await message.answer("Click command - /inline", reply_markup=menu_finl(message.from_user.id))
