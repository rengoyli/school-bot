from aiogram import Dispatcher

from handlers.user.help import bot_help
from handlers.user.start import bot_start, name_defined, class_letter_defined, \
    grade_defined  # , timetable, book, school_news
from states.user.user_info import UserInfo


def register_user_handler(dp: Dispatcher):
    dp.register_message_handler(bot_start, commands=['start'], state='*')
    dp.register_message_handler(name_defined, state=UserInfo.waiting_for_full_name)
    dp.register_message_handler(grade_defined, state=UserInfo.waiting_for_grade)
    dp.register_message_handler(class_letter_defined, state=UserInfo.waiting_for_class_letter)

    dp.register_message_handler(bot_help, commands=['help'])


def register_user_callback(dp: Dispatcher):
    ...
#     dp.register_callback_query_handler(timetable, text='timetable')
#     dp.register_callback_query_handler(book, text='book')
#     dp.register_callback_query_handler(school_news, text='school_news')
