# - *- coding: utf- 8 - *-
from aiogram import BaseMiddleware

from tgbot.database.db_users import Userx
from tgbot.utils.const_functions import clear_html


# Проверка юзера в БД и его добавление
class ExistsUserMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        this_user = data.get("event_from_user")

        if not this_user.is_bot:
            get_user = Userx.get(user_id=this_user.id)

            user_id = this_user.id
            user_login = this_user.username
            user_name = clear_html(this_user.first_name)
            user_surname = clear_html(this_user.last_name)
            user_fullname = clear_html(this_user.first_name)
            user_language = this_user.language_code

            if user_login is None: user_login = ""
            if user_name is None: user_name = ""
            if user_surname is None: user_surname = ""
            if user_fullname is None: user_fullname = ""
            if user_language != "ru": user_language = "en"

            if len(user_surname) >= 1: user_fullname += f" {user_surname}"

            if get_user is None:
                Userx.add(user_id, user_login.lower(), user_name, user_surname, user_fullname)
            else:
                if user_name != get_user.user_name:
                    Userx.update(get_user.user_id, user_name=user_name)

                if user_surname != get_user.user_surname:
                    Userx.update(get_user.user_id, user_surname=user_surname)

                if user_fullname != get_user.user_fullname:
                    Userx.update(get_user.user_id, user_fullname=user_fullname)

                if user_login.lower() != get_user.user_login:
                    Userx.update(get_user.user_id, user_login=user_login.lower())

            data['User'] = Userx.get(user_id=user_id)

        return await handler(event, data)
