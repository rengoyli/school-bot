from aiogram import Dispatcher
from aiogram.utils import exceptions
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from .errors.not_modified import message_not_modified, message_to_delete_not_found

from .user.start import bot_start
from .user.help import bot_help


def register_handlers(dp: Dispatcher):
    dp.register_errors_handler(message_not_modified, exception=exceptions.MessageNotModified)
    dp.register_errors_handler(message_to_delete_not_found, exception=exceptions.MessageToDeleteNotFound)

    dp.register_message_handler(bot_start, CommandStart)
    dp.register_message_handler(bot_help, CommandHelp)
