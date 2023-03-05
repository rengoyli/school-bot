from aiogram import types


def name(msg: types.Message) -> types.ReplyKeyboardMarkup:
    types.ReplyKeyboardRemove()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    tg_name_btn = msg.from_user.full_name

    keyboard.add(tg_name_btn)

    return keyboard


def grades() -> types.ReplyKeyboardMarkup:
    types.ReplyKeyboardRemove()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    _grades = [str(x) for x in range(1, 12)]

    keyboard.add(*_grades)

    return keyboard


def characters() -> types.ReplyKeyboardMarkup:
    types.ReplyKeyboardRemove()

    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    _characters = ['А', 'Б', 'В', 'Г']

    keyboard.add(*_characters)

    return keyboard
