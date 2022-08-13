# - *- coding: utf- 8 - *-
from aiogram import Bot
from aiogram.types import FSInputFile

from tgbot.config import get_admins, PATH_DATABASE
from tgbot.utils.const_functions import get_date, send_admins


# Выполнение функции после запуска бота (рассылка админам о запуске бота)
async def startup_notify(bot: Bot):
    if len(get_admins()) >= 1:
        await send_admins(bot, "<b>✅ Бот был запущен</b>")


# Автоматические бэкапы БД
async def autobackup(bot: Bot):
    for admin in get_admins():
        try:
            await bot.send_document(admin,
                                    FSInputFile(PATH_DATABASE),
                                    caption=f"<b>📦 AUTOBACKUP</b>\n"
                                            f"<code>🕰 {get_date()}</code>")
        except:
            pass
