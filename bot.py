import asyncio
import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.redis import RedisStorage2
from aiogram.types import BotCommand

from handlers import register_handlers
from filters import register_filters
# TODO: Add DependencyInjectMiddleware and fix KeyError: 'pg_pool'
# from middlewares import bind_middlewares

from data.config import BOT_TOKEN


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Старт"),
        BotCommand(command="/help", description="Помощь")
    ]
    await bot.set_my_commands(commands)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.error("Starting bot")

    bot = Bot(token=BOT_TOKEN, parse_mode="html")
    memory = RedisStorage2()
    dp = Dispatcher(bot, storage=memory)

    register_handlers(dp)
    register_filters(dp)
    # bind_middlewares(dp)

    await set_commands(bot)

    try:
        await dp.skip_updates()
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
