# - *- coding: utf- 8 - *-
from aiogram import Dispatcher, F

from tgbot.routers import main_errors, main_missed, main_start
from tgbot.routers.admin import admin_menu
from tgbot.routers.user import user_menu
from tgbot.utils.misc.bot_filters import IsAdmin


# Регистрация всех роутеров
def register_all_routers(dp: Dispatcher):
    # Подключение фильтров
    main_errors.router.message.filter(F.chat.type == "private")
    main_start.router.message.filter(F.chat.type == "private")
    main_missed.router.message.filter(F.chat.type == "private")

    user_menu.router.message.filter(F.chat.type == "private")

    admin_menu.router.message.filter(F.chat.type == "private", IsAdmin())

    # Подключение обязательных роутеров
    dp.include_router(main_errors.router)
    dp.include_router(main_start.router)

    # Подключение хендлеров (юзеров и админов)
    dp.include_router(user_menu.router)  # Юзер хендлер
    dp.include_router(admin_menu.router)  # Админ хендлер

    # Подключение обязательных роутеров
    dp.include_router(main_missed.router)
