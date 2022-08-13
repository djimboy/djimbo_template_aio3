# - *- coding: utf- 8 - *-
from aiogram import Router, Bot
from aiogram.types import FSInputFile, Message

from tgbot.config import PATH_DATABASE, PATH_LOGS
from tgbot.data.config import PATH_DATABASE, PATH_LOGS
from tgbot.keyboards.inline_misc import admin_inl
from tgbot.keyboards.reply_misc import admin_rep
from tgbot.utils.const_functions import get_date
from tgbot.utils.misc.bot_models import FSM, RS

router = Router()


# Кнопка - Admin Inline
@router.message(text="Admin Inline")
async def admin_button_inline(message: Message, bot: Bot, state: FSM, rSession: RS, my_user):
    await state.clear()

    await message.answer("Click Button - Admin Inline", reply_markup=admin_inl)


# Кнопка - Admin Reply
@router.message(text="Admin Reply")
async def admin_button_reply(message: Message, bot: Bot, state: FSM, rSession: RS, my_user):
    await state.clear()

    await message.answer("Click Button - Admin Reply", reply_markup=admin_rep)


# Получение Базы Данных
@router.message(commands=['db', 'database'])
async def admin_database(message: Message, bot: Bot, state: FSM, rSession: RS, my_user):
    await state.clear()

    await message.answer_document(FSInputFile(PATH_DATABASE),
                                  caption=f"<b>📦 BACKUP</b>\n"
                                          f"<code>🕰 {get_date()}</code>")


# Получение логов
@router.message(commands=['log', 'logs'])
async def admin_log(message: Message, bot: Bot, state: FSM, rSession: RS, my_user):
    await state.clear()

    await message.answer_document(FSInputFile(PATH_LOGS), caption=f"<code>🕰 {get_date()}</code>")
