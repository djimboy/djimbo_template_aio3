# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from tgbot.data.config import get_admins
from tgbot.utils.const_functions import rkb


# Кнопки главного меню
def menu_frep(user_id: int) -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()

    keyboard.row(
        rkb("User Inline"), rkb("User Reply"),
    )

    if user_id in get_admins():
        keyboard.row(
            rkb("Admin Inline"), rkb("Admin Reply"),
        )

    return keyboard.as_markup(resize_keyboard=True)
