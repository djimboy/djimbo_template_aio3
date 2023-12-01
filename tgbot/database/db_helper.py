# - *- coding: utf- 8 - *-
import sqlite3

from tgbot.data.config import PATH_DATABASE
from tgbot.utils.const_functions import ded


# Преобразование полученного списка в словарь
def dict_factory(cursor, row) -> dict:
    save_dict = {}

    for idx, col in enumerate(cursor.description):
        save_dict[col[0]] = row[idx]

    return save_dict


# Форматирование запроса без аргументов
def update_format(sql, parameters: dict) -> tuple[str, list]:
    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql += f" {values}"

    return sql, list(parameters.values())


# Форматирование запроса с аргументами
def update_format_where(sql, parameters: dict) -> tuple[str, list]:
    sql += " WHERE "

    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])

    return sql, list(parameters.values())


################################################################################
# Создание всех таблиц для БД
def create_dbx():
    with sqlite3.connect(PATH_DATABASE) as con:
        con.row_factory = dict_factory

        ############################################################
        # Создание таблицы с хранением - пользователей
        if len(con.execute("PRAGMA table_info(storage_users)").fetchall()) == 7:
            print("DB was found(1/2)")
        else:
            con.execute(
                ded(f"""
                    CREATE TABLE storage_users(
                        increment INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id INTEGER,
                        user_login TEXT,
                        user_name TEXT,
                        user_surname TEXT,
                        user_fullname TEXT,
                        user_unix INTEGER
                    )
                """)
            )
            print("DB was not found(1/2) | Creating...")

        # Создание таблицы с хранением - настроек
        if len(con.execute("PRAGMA table_info(storage_settings)").fetchall()) == 1:
            print("DB was found(2/2)")
        else:
            con.execute(
                ded(f"""
                    CREATE TABLE storage_settings(
                        status_work TEXT
                    )
                """)
            )

            con.execute(
                ded(f"""
                    INSERT INTO storage_settings(
                        status_work
                    )
                    VALUES (?)
                """),
                [
                    'True',
                ]
            )
            print("DB was not found(2/2) | Creating...")
