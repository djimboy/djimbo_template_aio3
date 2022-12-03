# - *- coding: utf- 8 - *-
import random
import time
from datetime import datetime
from typing import Union

from aiogram import Bot, types
from aiogram.types import InlineKeyboardButton, KeyboardButton

from tgbot.data.config import get_admins


######################################## AIOGRAM ########################################
# Генерация реплай кнопки
def rkb(text: str) -> KeyboardButton:
    return KeyboardButton(text=text)


# Генерация инлайн кнопки
def ikb(text: str, data: str = None, url: str = None, switch: str = None) -> InlineKeyboardButton:
    if data is not None:
        return InlineKeyboardButton(text=text, callback_data=data)
    elif url is not None:
        return InlineKeyboardButton(text=text, url=url)
    else:
        return InlineKeyboardButton(text=text, switch_inline_query=switch)


# Отправка сообщения всем админам
async def send_admins(bot: Bot, text: str, markup=None, not_me=0):
    for admin in get_admins():
        try:
            if str(admin) != str(not_me):
                await bot.send_message(admin, text, reply_markup=markup, disable_web_page_preview=True)
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
        await bot.send_dice(user_id, emoji=message.dice.emoji, reply_markup=reply)
    elif message.location is not None:
        await bot.send_location(user_id, latitude=message.location.latitude, longitude=message.location.longitude,
                                reply_markup=reply)
    else:
        await bot.send_message(user_id, get_text)


######################################## ПРОЧЕЕ ########################################
# Удаление отступов у текста
def ded(get_text: str) -> str:
    if get_text is not None:
        split_text = get_text.split("\n")
        if split_text[0] == "": split_text.pop(0)
        if split_text[-1] == "": split_text.pop(-1)
        save_text = []

        for text in split_text:
            while text.startswith(" "):
                text = text[1:]

            save_text.append(text)
        get_text = "\n".join(save_text)
    else:
        get_text = ""

    return get_text


# Очистка текста от HTML тэгов
def clear_html(get_text: str) -> str:
    if get_text is not None:
        if "<" in get_text: get_text = get_text.replace("<", "*")
        if ">" in get_text: get_text = get_text.replace(">", "*")
    else:
        get_text = ""

    return get_text


# Очистка пробелов в списке
def clear_list(get_list: list) -> list:
    while "" in get_list: get_list.remove("")
    while " " in get_list: get_list.remove(" ")
    while "," in get_list: get_list.remove(",")
    while "\r" in get_list: get_list.remove("\r")

    return get_list


# Разбив списка на несколько частей
def split_messages(get_list: list, count: int) -> list[list]:
    return [get_list[i:i + count] for i in range(0, len(get_list), count)]


# Получение даты
def get_date() -> str:
    return datetime.today().replace(microsecond=0).strftime("%d.%m.%Y %H:%M:%S")


# Получение юникс даты
def get_unix(full=False) -> int:
    if full:
        return time.time_ns()
    else:
        return int(time.time())


# Генерация пароля
def gen_password(len_password: int = 16, type_password: str = "default") -> str:  # default, number, letter, onechar
    if type_password == "default":
        char_password = list("1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")
    elif type_password == "letter":
        char_password = list("abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")
    elif type_password == "number":
        char_password = list("1234567890")
    elif type_password == "onechar":
        char_password = list("1234567890")

    random.shuffle(char_password)
    random_chars = "".join([random.choice(char_password) for x in range(len_password)])

    if type_password == "onechar":
        random_chars = f"{random.choice('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ')}{random_chars[1:]}"

    return random_chars


# Корректный вывод времени
def convert_times(get_time, get_type="day") -> str:
    get_time = int(get_time)
    if get_time < 0: get_time = 0

    if get_type == "second":
        get_list = ['секунда', 'секунды', 'секунд']
    elif get_type == "minute":
        get_list = ['минута', 'минуты', 'минут']
    elif get_type == "hour":
        get_list = ['час', 'часа', 'часов']
    elif get_type == "day":
        get_list = ['день', 'дня', 'дней']
    elif get_type == "month":
        get_list = ['месяц', 'месяца', 'месяцев']
    else:
        get_list = ['год', 'года', 'лет']

    if get_time % 10 == 1 and get_time % 100 != 11:
        count = 0
    elif 2 <= get_time % 10 <= 4 and (get_time % 100 < 10 or get_time % 100 >= 20):
        count = 1
    else:
        count = 2

    return f"{get_time} {get_list[count]}"


######################################## ЧИСЛА ########################################
# Преобразование длинных вещественных чисел в читаемый вид
def snum(amount, remains=0) -> str:
    if "-" in str(amount):
        str_amount = "%.*f" % (int(str(amount).split("-")[1]), amount)
    elif "." in str(amount):
        str_amount = f"{float(amount):.{len(str(amount).split('.')[1])}f}"
    else:
        str_amount = str(amount)

    if "." in str_amount:
        while str_amount.endswith('0'): str_amount = str_amount[:-1]
    if str_amount.endswith('.'): str_amount = str_amount[:-1]

    if remains != 0:
        str_amount = round(float(str_amount), remains)

    return str(str_amount)


# Конвертация числа в вещественное
def to_float(get_number, remains=2) -> Union[int, float]:
    if "," in str(get_number):
        get_number = str(get_number).replace(",", ".")

    if "." in str(get_number):
        get_last = str(get_number).split(".")

        if str(get_last[1]).endswith("0"):
            while True:
                if str(get_number).endswith("0"):
                    get_number = str(get_number)[:-1]
                else:
                    break

        get_number = round(float(get_number), remains)

    str_number = snum(get_number)
    if "." in str_number:
        if str_number.split(".")[1] == "0":
            get_number = int(get_number)
        else:
            get_number = float(get_number)
    else:
        get_number = int(get_number)

    return get_number


# Конвертация числа в целочисленное
def to_int(get_number) -> int:
    if "," in get_number:
        get_number = str(get_number).replace(",", ".")

    get_number = int(round(float(get_number)))

    return get_number


# Проверка числа на вещественное
def is_number(get_number) -> bool:
    if str(get_number).isdigit():
        return False
    else:
        if "," in str(get_number): get_number = str(get_number).replace(",", ".")

        try:
            float(get_number)
            return False
        except ValueError:
            return True


# Форматирование числа в читаемый вид
def format_rate(amount: Union[float, int], around: int = 2) -> str:
    if "," in str(amount): amount = float(str(amount).replace(",", "."))
    if " " in str(amount): amount = float(str(amount).replace(" ", ""))
    amount = str(round(amount, around))

    out_amount, save_remains = [], ""

    if "." in amount: save_remains = amount.split(".")[1]
    save_amount = [char for char in str(int(float(amount)))]

    if len(save_amount) % 3 != 0:
        if (len(save_amount) - 1) % 3 == 0:
            out_amount.extend([save_amount[0]])
            save_amount.pop(0)
        elif (len(save_amount) - 2) % 3 == 0:
            out_amount.extend([save_amount[0], save_amount[1]])
            save_amount.pop(0)
            save_amount.pop(1)
        else:
            print("Error 4388326")

    for x, char in enumerate(save_amount):
        if x % 3 == 0: out_amount.append(" ")
        out_amount.append(char)

    return "".join(out_amount).strip() + "." + save_remains
