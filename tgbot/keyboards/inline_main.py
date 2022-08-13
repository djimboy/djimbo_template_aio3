# - *- coding: utf- 8 - *-
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.data.config import get_admins
from tgbot.utils.const_functions import ikb


# Кнопки инлайн меню
def menu_finl(user_id):
    keyboard = InlineKeyboardBuilder(
    ).row(
        ikb("User 1", data="..."),
        ikb("User 2", data="...")
    )

    if user_id in get_admins():
        keyboard.row(
            ikb("Admin 1", data="..."),
            ikb("Admin 2", data="...")
        )

    return keyboard.as_markup()
