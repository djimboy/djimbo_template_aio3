# - *- coding: utf- 8 - *-
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from tgbot.utils.const_functions import rkb

# Тестовые админ реплай кнопки
admin_rep = ReplyKeyboardBuilder(
).row(
    rkb("Admin Reply 1"),
    rkb("Admin Reply 2"),
).row(
    rkb("🔙 Main menu"),
).as_markup(resize_keyboard=True)

# Тестовые юзер реплай кнопки
user_rep = ReplyKeyboardBuilder(
).row(
    rkb("User Reply 1"),
    rkb("User Reply 2"),
).row(
    rkb("🔙 Main menu"),
).as_markup(resize_keyboard=True)
