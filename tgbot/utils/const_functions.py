# - *- coding: utf- 8 - *-
import random
import time
from datetime import datetime

from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, KeyboardButton

######################################## AIOGRAM ########################################
# Генерация реплай кнопки
from tgbot.config import get_admins


def rkb(text):
    return KeyboardButton(text=text)


# Генерация инлайн кнопки
def ikb(text, data=None, url=None, switch=None):
    if data is not None:
        return InlineKeyboardButton(text=text, callback_data=data)
    elif url is not None:
        return InlineKeyboardButton(text=text, url=url)
    else:
        return InlineKeyboardButton(text=text, switch_inline_query=switch)


# Отправка сообщения всем админам
async def send_admins(bot: Bot, message, markup=None, not_me=0):
    for admin in get_admins():
        try:
            if str(admin) != str(not_me):
                await bot.send_message(admin, message, reply_markup=markup, disable_web_page_preview=True)
        except:
            pass


# Умная отправка сообщений
async def smart_send(bot: Bot, message: types.Message, user_id, text_add=None, reply=None):
    if message.text is not None:
        get_text = message.text
    elif message.caption is not None:
        get_text = message.caption
    else:
        get_text = ""

    if text_add is not None:
        get_text = text_add.format(get_text)

    if message.photo is not None:
        await bot.send_photo(user_id, message.photo[-1].file_id, caption=get_text, reply_markup=reply)
    elif message.video is not None:
        await bot.send_video(user_id, message.video.file_id, caption=get_text, reply_markup=reply)
    elif message.document is not None:
        await bot.send_document(user_id, message.document.file_id, caption=get_text, reply_markup=reply)
    elif message.audio is not None:
        await bot.send_audio(user_id, message.audio.file_id, caption=get_text, reply_markup=reply)
    elif message.voice is not None:
        await bot.send_voice(user_id, message.voice.file_id, caption=get_text, reply_markup=reply)
    elif message.animation is not None:
        await bot.send_animation(user_id, message.animation.file_id, reply_markup=reply)
    elif message.sticker is not None:
        await bot.send_sticker(user_id, message.sticker.file_id, reply_markup=reply)
    elif message.dice is not None:
        await bot.send_dice(user_id, message.dice.emoji, reply_markup=reply)
    elif message.location is not None:
        await bot.send_location(user_id, latitude=message.location.latitude, longitude=message.location.longitude,
                                reply_markup=reply)
    else:
        await bot.send_message(user_id, get_text)


######################################## ПРОЧЕЕ ########################################
# Очистка HTML тэгов
def clear_html(get_text: str):
    if get_text is not None:
        if "<" in get_text: get_text = get_text.replace("<", "*")
        if ">" in get_text: get_text = get_text.replace(">", "*")

    return get_text


# Очистка пробелов в списке
def clear_list(get_list: list):
    while "" in get_list: get_list.remove("")
    while " " in get_list: get_list.remove(" ")
    while "," in get_list: get_list.remove(",")
    while "\r" in get_list: get_list.remove("\r")

    return get_list


# Разбив списка на несколько частей
def split_messages(get_list: list, count: int):
    return [get_list[i:i + count] for i in range(0, len(get_list), count)]


# Получение даты
def get_date():
    this_date = datetime.today().replace(microsecond=0)
    this_date = this_date.strftime("%d.%m.%Y %H:%M:%S")

    return this_date


# Получение юникс даты
def get_unix():
    return int(time.time())


# Генерация пароля
def generate_password(len_password: int):
    passwd = list("1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")
    random.shuffle(passwd)
    random_chars = "".join([random.choice(passwd) for x in range(len_password)])

    return random_chars


# Корректный вывод времени
def convert_times(get_time, get_type="day"):
    get_time = int(get_time)

    if get_type == "second":
        get_list = ["секунда", "секунды", "секунд"]
    elif get_type == "minute":
        get_list = ["минута", "минуты", "минут"]
    elif get_type == "hour":
        get_list = ["час", "часа", "часов"]
    elif get_type == "day":
        get_list = ["день", "дня", "дней"]
    elif get_type == "month":
        get_list = ["месяц", "месяца", "месяцев"]
    else:
        get_list = ["год", "года", "лет"]

    if get_time % 10 == 1 and get_time % 100 != 11:
        count = 0
    elif 2 <= get_time % 10 <= 4 and (get_time % 100 < 10 or get_time % 100 >= 20):
        count = 1
    else:
        count = 2

    return f"{get_time} {get_list[count]}"


######################################## ЧИСЛА ########################################
# Конвертация числа в вещественное
def to_float(get_number, remains=2):
    if "," in str(get_number):
        get_number = str(get_number).replace(",", ".")

    if "." in get_number:
        get_last = get_number.split(".")

        if get_last[1].endswith("0"):
            while True:
                if get_number.endswith("0"):
                    get_number = get_number[:-1]
                else:
                    break

        get_number = round(float(get_number), remains)

    if str(float(get_number)).split(".")[1] == "0":
        get_number = int(get_number)
    else:
        get_number = float(get_number)

    return get_number


# Конвертация числа в целочисленное
def to_int(get_number):
    if "," in get_number:
        get_number = get_number.replace(",", ".")

    get_number = int(round(float(get_number)))

    return get_number


# Проверка числа на вещественное
def is_number(get_number):
    if get_number.isdigit():
        return False
    else:
        if "," in str(get_number): get_number = str(get_number).replace(",", ".")

        try:
            float(get_number)
            return False
        except ValueError:
            return True


# Преобразование длинных вещественных чисел в читаемый вид
def show_floats(amount):
    return f"{float(amount):.{len(str(amount).split('.')[1])}f}"


# Форматирование чисел в читаемый вид
def format_rate(rate, around=False):
    rate = str(round(float(rate), 2))

    if "," in rate:
        rate = float(rate.replace(",", "."))

    len_rate = str(int(float(rate)))

    if len(len_rate) == 3:
        get_rate = str(len_rate)
    elif len(len_rate) == 4:
        get_rate = f"{len_rate[0]} {len_rate[1:]}"
    elif len(len_rate) == 5:
        get_rate = f"{len_rate[0:2]} {len_rate[2:]}"
    elif len(len_rate) == 6:
        get_rate = f"{len_rate[0:3]} {len_rate[3:]}"
    elif len(len_rate) == 7:
        get_rate = f"{len_rate[0:1]} {len_rate[1:4]} {len_rate[4:]}"
    elif len(len_rate) == 8:
        get_rate = f"{len_rate[0:2]} {len_rate[2:5]} {len_rate[5:]}"
    elif len(len_rate) == 9:
        get_rate = f"{len_rate[0:3]} {len_rate[3:6]} {len_rate[6:]}"
    elif len(len_rate) == 10:
        get_rate = f"{len_rate[0:1]} {len_rate[1:4]} {len_rate[4:7]} {len_rate[7:]}"
    else:
        get_rate = 0

    if not around:
        if "." in rate:
            dot_amount = rate.find(".")
            get_rate += f"{rate[dot_amount:]}"

    return get_rate
