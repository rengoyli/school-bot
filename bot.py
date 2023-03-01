import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from handlers import register_handlers
from filters import register_filters
# TODO: Add DependencyInjectMiddleware and fix KeyError: 'pg_pool'
# from middlewares import bind_middlewares , DependencyInjectMiddleware


from data.config import BOT_TOKEN


async def on_startup(dp: Dispatcher):
    register_handlers(dp)
    register_filters(dp)

    logging.info("[2 / 2] Bot started")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    memory = MemoryStorage()
    bot = Bot(token=BOT_TOKEN, parse_mode="html")
    dp = Dispatcher(bot, storage=memory)

    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
