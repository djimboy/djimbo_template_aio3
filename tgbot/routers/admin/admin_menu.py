# - *- coding: utf- 8 - *-
from aiogram import Router, Bot
from aiogram.filters import Text, Command
from aiogram.types import FSInputFile, Message, CallbackQuery

from tgbot.data.config import PATH_DATABASE, PATH_LOGS
from tgbot.keyboards.inline_misc import admin_inl
from tgbot.keyboards.reply_misc import admin_rep
from tgbot.utils.const_functions import get_date
from tgbot.utils.misc.bot_models import FSM, AS

router = Router()


# Кнопка - Admin Inline
@router.message(Text(text="Admin Inline"))
async def admin_button_inline(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await state.clear()

    await message.answer("Click Button - Admin Inline", reply_markup=admin_inl)


# Кнопка - Admin Reply
@router.message(Text(text="Admin Reply"))
async def admin_button_reply(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await state.clear()

    await message.answer("Click Button - Admin Reply", reply_markup=admin_rep)


# Колбэк - Admin X
@router.callback_query(Text(text="admin_inline_x"))
async def admin_callback_inline_x(call: CallbackQuery, bot: Bot, state: FSM, aSession: AS, my_user):
    await call.answer(f"Click Admin X")


# Колбэк - Admin
@router.callback_query(Text(startswith="admin_inline:"))
async def admin_callback_inline(call: CallbackQuery, bot: Bot, state: FSM, aSession: AS, my_user):
    get_data = call.data.split(":")[1]

    await call.answer(f"Click Admin - {get_data}", True)


# Получение Базы Данных
@router.message(Command(commands=['db', 'database']))
async def admin_database(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await state.clear()

    await message.answer_document(FSInputFile(PATH_DATABASE),
                                  caption=f"<b>📦 BACKUP</b>\n"
                                          f"🕰 <code>{get_date()}</code>")


# Получение логов
@router.message(Command(commands=['log', 'logs']))
async def admin_log(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await state.clear()

    await message.answer_document(FSInputFile(PATH_LOGS),
                                  caption=f"<b>🖨 LOGS</b>\n"
                                          f"🕰 <code>{get_date()}</code>")


# Очистить логи
@router.message(Command(commands=['clear_log', 'clear_logs', 'log_clear', 'logs_clear']))
async def admin_logs_clear(message: Message, bot: Bot, state: FSM, aSession: AS, my_user):
    await state.clear()

    with open(PATH_LOGS, "w") as file:
        file.write(f"{get_date()} | LOGS WAS CLEAR")

    await message.answer("<b>🖨 Логи были успешно очищены</b>")
