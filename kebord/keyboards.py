from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keybord_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Отправь фото мяу мяу')
    button_2 = KeyboardButton('Переход на другую клавеатуру')
    keyboard.add(button_1, button_2)
    return keyboard


def get_keybord_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_3 = KeyboardButton('Отправь фото тяф тяф')
    button_4 = KeyboardButton('Переход обратно')
    keyboard_2.add(button_3, button_4)
    return keyboard_2


