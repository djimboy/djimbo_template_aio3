# - *- coding: utf- 8 - *-
from aiogram import Router, Bot
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Update

from tgbot.utils.misc.bot_logging import bot_logger
from tgbot.utils.misc_functions import send_admins

router = Router()


# Обработка ошибок
@router.errors()
async def processing_errors(update: Update, exception: TelegramAPIError, bot: Bot):
    print(f"-Exception | {exception}")
    await send_admins(bot, f"<b>❌ Ошибка\n\n"
                           f"<b>Exception: <code>{exception}</code>\n\n"
                           f"Update: <code>{update.dict()}</code></b>")

    bot_logger.exception(
        f"Exception: {exception}\n"
        f"Update: {update.dict()}"
    )
