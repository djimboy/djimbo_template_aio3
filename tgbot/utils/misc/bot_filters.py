# - *- coding: utf- 8 - *-
from aiogram.filters import BaseFilter
from aiogram.types import Message

from tgbot.data.config import get_admins


# Проверка на админа
class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.from_user.id in get_admins():
            return True
        else:
            return False
