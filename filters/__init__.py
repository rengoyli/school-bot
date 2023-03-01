from aiogram import Dispatcher

from .is_admin import AdminFilter


def register_filters(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)
