# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.data.config import get_admins
from tgbot.utils.const_functions import ikb


# Кнопки инлайн меню
def menu_finl(user_id: int) -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardBuilder()

    keyboard.row(
        ikb("User X", data="user_inline_x"),
        ikb("User 1", data="user_inline:user_btn"),
        ikb("User 2", data="..."),
    )

    if user_id in get_admins():
        keyboard.row(
            ikb("Admin X", data="admin_inline_x"),
            ikb("Admin 1", data="admin_inline:admin_btn"),
            ikb("Admin 2", data="unknown"),
        )

    return keyboard.as_markup()
