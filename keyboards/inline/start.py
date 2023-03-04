from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def user_menu() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(row_width=2)
    buttons = [
        types.InlineKeyboardButton(text='Расписание', callback_data='timetable'),
        types.InlineKeyboardButton(text='Книги', callback_data='book'),
        types.InlineKeyboardButton(text='Школьные новости', callback_data='school_news'),
    ]
    keyboard.add(*buttons)

    return keyboard
