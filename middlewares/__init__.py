from aiogram import Dispatcher
from middlewares.throttling import ThrottlingMiddleware


def bind_middlewares(dp: Dispatcher):
    dp.middleware.setup(
        ThrottlingMiddleware(5)
    )
