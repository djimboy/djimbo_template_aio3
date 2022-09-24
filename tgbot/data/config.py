# - *- coding: utf- 8 - *-
import configparser

from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Токен бота
BOT_TOKEN = configparser.ConfigParser(timezone="Europe/Moscow")
BOT_TOKEN.read("settings.ini")
BOT_TOKEN = BOT_TOKEN['settings']['token'].strip().replace(' ', '')

# Пути к файлам
PATH_DATABASE = "tgbot/data/database.db"  # Путь к БД
PATH_LOGS = "tgbot/data/logs.log"  # Путь к Логам

# Образы и конфиги
scheduler = AsyncIOScheduler(timezone="Europe/Moscow")  # Образ шедулера
start_status = True  # Оповещение админам при запуске бота (True или False)


# Получение администраторов бота
def get_admins():
    read_admins = configparser.ConfigParser()
    read_admins.read('settings.ini')

    admins = read_admins['settings']['admin_id'].strip().replace(' ', '')

    if ',' in admins:
        admins = admins.split(',')
    else:
        if len(admins) >= 1:
            admins = [admins]
        else:
            admins = []

    while "" in admins: admins.remove("")
    while " " in admins: admins.remove(" ")
    while "," in admins: admins.remove(",")
    while "\r" in admins: admins.remove("\r")

    admins = list(map(int, admins))

    return admins
