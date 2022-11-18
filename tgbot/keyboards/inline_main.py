# - *- coding: utf- 8 - *-
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.data.config import get_admins
from tgbot.utils.const_functions import ikb


# Кнопки инлайн меню
def menu_finl(user_id):
    keyboard = InlineKeyboardBuilder(
    ).row(
        ikb("User X", data="user_inline_x"),
        ikb("User 1", data="user_inline:1"),
        ikb("User 2", data="user_inline:2"),
    )

    if user_id in get_admins():
        keyboard.row(
            ikb("Admin X", data="admin_inline_x"),
            ikb("Admin 1", data="admin_inline:1"),
            ikb("Admin 2", data="admin_inline:2"),
        )

    return keyboard.as_markup()
