# - *- coding: utf- 8 - *-
import sqlite3

from tgbot.data.config import PATH_DATABASE
from tgbot.utils.const_functions import get_unix


# Преобразование БД словаря
def dict_factory(cursor, row) -> dict:
    this_dict = {}

    for idx, col in enumerate(cursor.description):
        this_dict[col[0]] = row[idx]

    return this_dict


################################################################################
########################### ФОРМАТИРОВАНИЕ ЗАПРОСОВ ############################
# Форматирование запроса без аргументов
def update_format(sql, parameters: dict) -> tuple[str, list]:
    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql += f" {values}"

    return sql, list(parameters.values())


# Форматирование запроса с аргументами
def update_format_args(sql, parameters: dict) -> tuple[str, list]:
    sql += " WHERE "

    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])

    return sql, list(parameters.values())


############################# ЗАПРОСЫ К БАЗЕ ДАННЫХ ############################
################################################################################
# Добавление пользователя
def add_userx(user_id, user_login, user_name, user_surname, user_fullname):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        con.execute(
            "INSERT INTO storage_users "
            "(user_id, user_login, user_name, user_surname, user_fullname, user_unix) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            [user_id, user_login, user_name, user_surname, user_fullname, get_unix()],
        )


# Получение пользователя
def get_userx(**kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = "SELECT * FROM storage_users"
        sql, parameters = update_format_args(sql, kwargs)

        return con.execute(sql, parameters).fetchone()


# Получение пользователей
def get_usersx(**kwargs) -> list[dict]:
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = "SELECT * FROM storage_users"
        sql, parameters = update_format_args(sql, kwargs)

        return con.execute(sql, parameters).fetchall()


# Получение всех пользователей
def get_all_usersx() -> list[dict]:
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = "SELECT * FROM storage_users"

        return con.execute(sql).fetchall()


# Редактирование пользователя
def update_userx(user_id, **kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = f"UPDATE storage_users SET"
        sql, parameters = update_format(sql, kwargs)
        parameters.append(user_id)
        con.execute(sql + "WHERE user_id = ?", parameters)


# Удаление пользователя
def delete_userx(**kwargs):
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory
        sql = "DELETE FROM storage_users"
        sql, parameters = update_format_args(sql, kwargs)
        con.execute(sql, parameters)


############################## СОЗДАНИЕ БАЗЫ ДАННЫХ ############################
# Создание всех таблиц для Базы Данных
def create_dbx():
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory

        # Таблица с хранением пользователей
        if len(con.execute("PRAGMA table_info(storage_users)").fetchall()) == 7:
            print("DB was found(1/1)")
        else:
            con.execute(
                "CREATE TABLE storage_users("
                "increment INTEGER PRIMARY KEY AUTOINCREMENT, "
                "user_id INTEGER,"
                "user_login TEXT,"
                "user_name TEXT,"
                "user_surname TEXT,"
                "user_fullname TEXT,"
                "user_unix INTEGER"
                ")"
            )
            print("DB was not found(1/1) | Creating...")
