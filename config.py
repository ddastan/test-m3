from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

TOKEN="7601468161:AAH0gaYJPAT6kiBPzFe1MphmfPFqoNn56jI"

staff = [6554760070, ]

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
