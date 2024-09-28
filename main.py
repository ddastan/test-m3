import logging
from aiogram.utils import executor
from handlers import  echo, FSM_reg, fsm_store, send_products, commands
from config import dp, bot, staff
from db import db_main


async def on_startup(_):
    for admin in staff:
        await bot.send_message(chat_id=admin, text="Бот включен!")
        await db_main.sql_create()


async def on_shutdown(_):
    for admin in staff:
        await bot.send_message(chat_id=admin, text="Бот отключен!")



FSM_reg.register_fsm_reg(dp)
fsm_store.register_store(dp)

send_products.register_send_products_handler(dp)


echo.register_echo(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True,
                           on_startup=on_startup, on_shutdown=on_shutdown)