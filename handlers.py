from aiogram import types, Router
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import markup
import texts


router = Router()
#@router.message(Command('start'))
#async def start_command(msg:Message):
    #await msg.answer("Привет!\n это бот по менеджменту POSM")
    #await msg.answer(texts.menu, reply_markup=markup.menu)


@router.message(Command('info'))
async def help_command(msg:Message):
    await msg.answer("Привет!\n Это бот по менеджменту POSM\nЭта команда покажет все функции бота")

@router.message(Command('menu'))
async def menu(msg:Message):
    await msg.answer(texts.menu, reply_markup=markup.menu)


@router.callback_query()
async def button_handler(callback_query: types.CallbackQuery):
    if callback_query.data == 'create_request':
        return await callback_query.answer(text = 'Ты хочешь создать новую заявку')

#    if button_data == 'create_request':
#        await bot.send_message(callback_query.message.chat.id, 'Button 1 pressed!')
#@router.message(Command('create_request'))
#async def create_request(msg:Message):
#    await msg.answer(texts.city, reply_markup=markup.create_requests)