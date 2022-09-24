# - *- coding: utf- 8 - *-
from aiogram import BaseMiddleware

from tgbot.services.api_sqlite import get_userx, add_userx, update_userx
from tgbot.utils.const_functions import clear_html


# Проверка юзера в БД и его добавление
class ExistsUserMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        this_user = data.get("event_from_user")

        if not this_user.is_bot:
            get_user = get_userx(user_id=this_user.id)

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
                add_userx(user_id, user_login.lower(), user_name, user_surname, user_fullname)
            else:
                if user_name != get_user['user_name']:
                    update_userx(get_user['user_id'], user_name=user_name)

                if user_surname != get_user['user_surname']:
                    update_userx(get_user['user_id'], user_surname=user_surname)

                if user_fullname != get_user['user_fullname']:
                    update_userx(get_user['user_id'], user_fullname=user_fullname)

                if user_login.lower() != get_user['user_login']:
                    update_userx(get_user['user_id'], user_login=user_login.lower())

            data['my_user'] = get_userx(user_id=user_id)

        return await handler(event, data)
