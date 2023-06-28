from aiogram import types, Router, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import markup
import texts
from aiogram.filters.callback_data import CallbackData
from aiogram.filters import Text
import sqlite3
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton
from typing import List

#class MyCallback(CallbackData):
#   foo: str
#   bar: str

#button_callback = MyCallback(foo = 'button', bar = 'option')

router = Router()


@router.message(Command('info'))
async def help_command(msg:Message):
    await msg.answer("Привет!\nЭто бот по менеджменту POSM")

#@router.message(Command('start'))
#async def cmd_start(msg:Message):
#    await msg.answer(texts.start, reply_markup=markup.menu_kb)


#menu_btns[1][0] - second row
#@router.message(Text(markup.menu_btns[0][0].text))
#async def msg_city_handler(message: types.Message):
#   await message.answer("Выберите город", reply_markup=markup.city_kb)

#@router.message(Text(markup.city_btns[0][0].text))
#async def msg_store_handler(message: types.Message):
#    await message.answer("Выберите магазин", reply_markup=markup.store_kb)


@router.message(Command('start'))
async def start_command(message: types.Message):
    # Establish a connection to the SQLite database
    conn = sqlite3.connect('db.db')
    cursor = conn.cursor()

    # Retrieve the data from the database tables
    cursor.execute('SELECT * FROM cities')
    cities = cursor.fetchall()

    cursor.execute('SELECT * FROM stores')
    stores = cursor.fetchall()

    cursor.execute('SELECT * FROM repairment_types')
    repairments = cursor.fetchall()

    # Close the database connection
    conn.close()

    # Create the message string
    message_str = 'Cities:\n'
    for city in cities:
        message_str += f'- {city[1]}\n'

    message_str += '\nStores:\n'
    for store in stores:
        message_str += f'- {store[1]}\n'

    message_str += '\nrepairment_types:\n'
    for repairment in repairments:
        message_str += f'- {repairment[1]}\n'

    # Send the message to the user
    await message.answer(message_str)

