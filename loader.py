from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.postgral import Database


bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

db= Database()

# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage

# from data import config
# from utils.db_api.postgral import Database

# bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML,)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)


# db= Database()

# PROXY_URL = "http://proxy.server:3128"

# bot = Bot(proxy=PROXY_URL)