from aiogram import Dispatcher

from handlers.user.help import bot_help
from handlers.user.start import bot_start, timetable


def register_user(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(bot_help, commands=['help'])


def register_user_callback(dp: Dispatcher):
    dp.register_callback_query_handler(timetable, text='timetable')