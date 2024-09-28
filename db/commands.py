import os
from aiogram.types import InputFile
from buttons import start
from config import dp, bot
from aiogram import types, Dispatcher


async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, 'Hello!',
                           reply_markup=start)

async def info_handler(message: types.Message):
    await message.answer('Саламалейкум радной, шаву поставь по братски')



def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])
