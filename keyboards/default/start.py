from aiogram import types


def tg_name_btn(msg: types.Message) -> types.ReplyKeyboardMarkup:
    types.ReplyKeyboardRemove()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    _tg_name_btn = msg.from_user.full_name

    keyboard.add(_tg_name_btn)

    return keyboard


def grades_btn() -> types.ReplyKeyboardMarkup:
    types.ReplyKeyboardRemove()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    _grades = [str(x) for x in range(1, 12)]

    keyboard.add(*_grades)

    return keyboard


def class_letters_btn() -> types.ReplyKeyboardMarkup:
    types.ReplyKeyboardRemove()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    _class_letters = ['А', 'Б', 'В', 'Г']

    keyboard.add(*_class_letters)

    return keyboard
