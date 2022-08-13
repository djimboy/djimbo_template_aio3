# - *- coding: utf- 8 - *-
from aiogram.utils.keyboard import InlineKeyboardBuilder

from tgbot.utils.const_functions import ikb

# Тестовые админ инлайн кнопки
admin_inl = InlineKeyboardBuilder(
).row(
    ikb("Admin Inline 1", data="..."),
    ikb("Admin Inline 2", data="..."),
).row(
    ikb("Admin Inline 3", data="..."),
).as_markup()

# Тестовые юзер инлайн кнопки
user_inl = InlineKeyboardBuilder(
).row(
    ikb("User Inline 1", data="..."),
    ikb("User Inline 2", data="..."),
).row(
    ikb("User Inline 3", data="..."),
).as_markup()
