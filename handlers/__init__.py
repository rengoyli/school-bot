from aiogram import Dispatcher

from handlers.errors import register_errors
from handlers.user import register_user, register_user_callback


def register_handlers(dp: Dispatcher):
    register_errors(dp)
    register_user(dp)
    register_user_callback(dp)
