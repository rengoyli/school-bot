from aiogram import Dispatcher

from handlers.user.help import bot_help
from handlers.user.start import bot_start, timetable, book, school_news


def register_user_handler(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'])
    dp.register_message_handler(bot_help, commands=['help'])


def register_user_callback(dp: Dispatcher):
    dp.register_callback_query_handler(timetable, text='timetable')
    dp.register_callback_query_handler(book, text='book')
    dp.register_callback_query_handler(school_news, text='school_news')

