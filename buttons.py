from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

start = ReplyKeyboardMarkup(resize_keyboard=True,
                            row_width=2)

start_button = KeyboardButton('/start')
info_button = KeyboardButton('/info')


start.add(start_button, info_button)