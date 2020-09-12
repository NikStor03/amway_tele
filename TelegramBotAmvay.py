import asyncio
import os

from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

loop = asyncio.get_event_loop()
bot = Bot(str(os.environ.get("TOKEN")), parse_mode="HTML")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)

if __name__ == '__main__':
    from handlers import *

    executor.start_polling(dp, on_startup=handle_start)
