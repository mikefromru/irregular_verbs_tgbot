import asyncio
import logging
from aiogram import Bot, Dispatcher
import logging
from aiogram import types
from aiogram.types import BotCommand

from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import dotenv_values

config = dotenv_values(".env")

# mine
from handlers import client, verbs

storage = MemoryStorage()

async def on_startup(_):
    print('Running ...')

async def shutdown(_):
    await storage.close()
    await bot.close()

async def main():
    bot = Bot(token=config.get('TOKEN'), parse_mode='HTML')
    dp = Dispatcher(storage=storage)
    dp = Dispatcher()

    dp.include_routers(
            client.router,
            verbs.verbs_router,
        )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, on_startup=on_startup)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
