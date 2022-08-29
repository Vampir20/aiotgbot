from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot("5744131240:AAHD3QT_PoIRRuxAZfM0EtKU0r2scWSzy4Y")
dp = Dispatcher(bot, storage=storage)
