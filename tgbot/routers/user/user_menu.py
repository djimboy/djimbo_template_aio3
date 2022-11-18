# - *- coding: utf- 8 - *-
from aiogram import Router, Bot
from aiogram.filters import Command, Text
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.inline_main import menu_finl
from tgbot.keyboards.inline_misc import user_inl
from tgbot.keyboards.reply_misc import user_rep
from tgbot.utils.misc.bot_models import FSM, AS

router = Router()


# Кнопка - User Inline
@router.message(Text(text="User Inline"))
async def user_button_inline(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await state.clear()

    await message.answer("Click Button - User Inline", reply_markup=user_inl)


# Кнопка - User Reply
@router.message(Text(text="User Reply"))
async def user_button_reply(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await state.clear()

    await message.answer("Click Button - User Reply", reply_markup=user_rep)


# Команда - /inline
@router.message(Command(commands="inline"))
async def user_command_inline(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await state.clear()

    await message.answer("Click command - /inline", reply_markup=menu_finl(message.from_user.id))


# Колбэк - User X
@router.callback_query(Text(text="user_inline_x"))
async def user_callback_inline_x(call: CallbackQuery, bot: Bot, state: FSM, aSession: AS, my_user):
    await call.answer(f"Click User X")


# Колбэк - User
@router.callback_query(Text(startswith="user_inline:"))
async def user_callback_inline(call: CallbackQuery, bot: Bot, state: FSM, aSession: AS, my_user):
    get_data = call.data.split(":")[1]

    await call.answer(f"Click User - {get_data}", True)
