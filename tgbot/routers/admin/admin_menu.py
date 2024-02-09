# - *- coding: utf- 8 - *-
import os

import aiofiles
from aiogram import Router, Bot, F
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message, CallbackQuery
from aiogram.utils.media_group import MediaGroupBuilder

from tgbot.data.config import PATH_DATABASE, PATH_LOGS
from tgbot.database.db_users import UserModel
from tgbot.keyboards.inline_misc import admin_inl
from tgbot.keyboards.reply_misc import admin_rep
from tgbot.utils.const_functions import get_date
from tgbot.utils.misc.bot_models import FSM, ARS

router = Router(name=__name__)


# Кнопка - Admin Inline
@router.message(F.text == 'Admin Inline')
async def admin_button_inline(message: Message, bot: Bot, state: FSM, arSession: ARS, User: UserModel):
    await state.clear()

    await message.answer("Click Button - Admin Inline", reply_markup=admin_inl)


# Кнопка - Admin Reply
@router.message(F.text == 'Admin Reply')
async def admin_button_reply(message: Message, bot: Bot, state: FSM, arSession: ARS, User: UserModel):
    await state.clear()

    await message.answer("Click Button - Admin Reply", reply_markup=admin_rep)


# Колбэк - Admin X
@router.callback_query(F.data == 'admin_inline_x')
async def admin_callback_inline_x(call: CallbackQuery, bot: Bot, state: FSM, arSession: ARS, User: UserModel):
    await call.answer(f"Click Admin X")


# Колбэк - Admin
@router.callback_query(F.data.startswith('admin_inline:'))
async def admin_callback_inline(call: CallbackQuery, bot: Bot, state: FSM, arSession: ARS, User: UserModel):
    get_data = call.data.split(":")[1]

    await call.answer(f"Click Admin - {get_data}", True)


# Получение Базы Данных
@router.message(Command(commands=['db', 'database']))
async def admin_database(message: Message, bot: Bot, state: FSM, arSession: ARS, User: UserModel):
    await state.clear()

    await message.answer_document(
        FSInputFile(PATH_DATABASE),
        caption=f"<b>📦 #BACKUP | <code>{get_date()}</code></b>",
    )


# Получение логов
@router.message(Command(commands=['log', 'logs']))
async def admin_log(message: Message, bot: Bot, state: FSM, arSession: ARS, User: UserModel):
    await state.clear()

    media_group = MediaGroupBuilder(
        caption=f"<b>🖨 #LOGS | <code>{get_date(full=False)}</code></b>",
    )

    if os.path.isfile(PATH_LOGS):
        media_group.add_document(media=FSInputFile(PATH_LOGS))

    if os.path.isfile("tgbot/data/sv_log_err.log"):
        media_group.add_document(media=FSInputFile("tgbot/data/sv_log_err.log"))

    if os.path.isfile("tgbot/data/sv_log_out.log"):
        media_group.add_document(media=FSInputFile("tgbot/data/sv_log_out.log"))

    await message.answer_media_group(media=media_group.build())


# Очистить логи
@router.message(Command(commands=['clear_log', 'clear_logs', 'log_clear', 'logs_clear']))
async def admin_logs_clear(message: Message, bot: Bot, state: FSM, arSession: ARS, User: UserModel):
    await state.clear()

    if os.path.isfile(PATH_LOGS):
        async with aiofiles.open(PATH_LOGS, "w") as file:
            await file.write(f"{get_date()} | LOGS WAS CLEAR")

    if os.path.isfile("tgbot/data/sv_log_err.log"):
        async with aiofiles.open("tgbot/data/sv_log_err.log", "w") as file:
            await file.write(f"{get_date()} | LOGS WAS CLEAR")

    if os.path.isfile("tgbot/data/sv_log_out.log"):
        async with aiofiles.open("tgbot/data/sv_log_out.log", "w") as file:
            await file.write(f"{get_date()} | LOGS WAS CLEAR")

    await message.answer("<b>🖨 The logs have been cleared</b>")
