from aiogram import Dispatcher
from aiogram.utils import exceptions

from handlers.errors.not_modified import message_to_delete_not_found, message_not_modified


def register_errors(dp: Dispatcher):
    dp.register_errors_handler(message_not_modified, exception=exceptions.MessageNotModified)
    dp.register_errors_handler(message_to_delete_not_found, exception=exceptions.MessageToDeleteNotFound)
