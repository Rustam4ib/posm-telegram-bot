from aiogram import types, Router, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import markup
import texts
#from bot import Dispatcher
from aiogram.filters.callback_data import CallbackData
from aiogram.filters import Text

#class MyCallback(CallbackData):
#    foo: str
#    bar: str

#button_callback = MyCallback(foo = 'button', bar = 'option')


router = Router()
dp = Dispatcher()
#@router.message(Command('start'))
#async def start_command(msg:Message):
    #await msg.answer("Привет!\n это бот по менеджменту POSM")
    #await msg.answer(texts.menu, reply_markup=markup.menu)


@router.message(Command('info'))
async def help_command(msg:Message):
    await msg.answer("Привет!\nЭто бот по менеджменту POSM")

@router.message(Command('start'))
async def cmd_start(msg:Message):
    await msg.answer(texts.start, reply_markup=markup.menu_kb)


#menu_btns[1][0] - second row
@router.message(Text(markup.menu_btns[0][0].text))
async def msg_city_handler(message: types.Message):
    await message.answer("Выберите город", reply_markup=markup.city_kb)

@router.message(Text(markup.city_btns[0][0].text))
async def msg_store_handler(message: types.Message):
    await message.answer("Выберите магазин", reply_markup=markup.store_kb)

#@dp.callback_query_handler(button_callback.filter())
#async def handle_button_callback(query: CallbackQuery, callback_data: dict):
#    option = callback_data['option']
#    await query.answer(f'You selected Option {option}.')
#@router.callback_query()
#async def button_handler(query: types.CallbackQuery, callback_data: dict):

#    if button_data == 'create_request':
#        await bot.send_message(callback_query.message.chat.id, 'Button 1 pressed!')
#@router.message(Command('create_request'))
#async def create_request(msg:Message):
#    await msg.answer(texts.city, reply_markup=markup.create_requests)