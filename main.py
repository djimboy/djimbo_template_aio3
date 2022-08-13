# - *- coding: utf- 8 - *-
import asyncio
import os
import sys

import colorama
from aiogram import Bot, Dispatcher

from tgbot.config import BOT_TOKEN, scheduler, get_admins
from tgbot.middlewares import register_all_middlwares
from tgbot.routers import register_all_routers
from tgbot.services.api_session import RequestsSession
from tgbot.services.api_sqlite import create_dbx
from tgbot.utils.misc.bot_commands import set_commands
from tgbot.utils.misc.bot_logging import bot_logger
from tgbot.utils.misc_functions import autobackup, startup_notify

colorama.init()


# Запуск шедулеров
async def scheduler_start(bot):
    scheduler.add_job(autobackup, "cron", hour=00, args=(bot,))  # Автобэкап в 12:00
    scheduler.add_job(autobackup, "cron", hour=12, args=(bot,))  # Автобэкап в 00:00


# Запуск бота и функций
async def main():
    scheduler.start()  # Запуск Шедулера
    dp = Dispatcher()  # Создание Диспетчера
    rSession = RequestsSession()  # Асинхронные Запросы
    bot = Bot(token=BOT_TOKEN, parse_mode="HTML")  # Образ Бота

    register_all_middlwares(dp)  # Регистрация всех мидлварей
    register_all_routers(dp)  # Регистрация всех роутеров

    try:
        await set_commands(bot)
        await startup_notify(bot)
        await scheduler_start(bot)

        bot_logger.warning("Bot was started")
        print(colorama.Fore.LIGHTYELLOW_EX + "~~~~~ Bot was started ~~~~~")
        print(colorama.Fore.LIGHTBLUE_EX + "~~~~~ TG developer: @djimbox ~~~~~")
        print(colorama.Fore.RESET)

        if len(get_admins()) == 0: print("***** ENTER ADMIN ID IN settings.ini *****")

        await bot.delete_webhook()
        await bot.get_updates(offset=-1)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types(), rSession=rSession)
    finally:
        await rSession.close()
        await bot.session.close()


if __name__ == "__main__":
    create_dbx()

    try:
        # Исправление "RuntimeError: Event loop is closed" для Windows
        # if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith("win"):
        #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        bot_logger.warning("Bot was stopped")
    finally:
        if sys.platform.startswith("win"):
            os.system("cls")
        else:
            os.system("clear")