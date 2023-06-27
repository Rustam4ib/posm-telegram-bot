from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu_btns = [
    [KeyboardButton(text = 'Создать заявку',)],
    [KeyboardButton(text = 'Обновление')],
    [KeyboardButton(text = 'Фильтр заявок')],
    [KeyboardButton(text = 'Открыть заявку')]
    ]

city_btns = [
    [InlineKeyboardButton(text = 'Almaty', callback_data='almaty')],
    [InlineKeyboardButton(text = 'Astana', callback_data='astana')],
    [InlineKeyboardButton(text = 'Karaganda', callback_data='karaganda')],
    [InlineKeyboardButton(text = 'Aktobe', callback_data='aktobe')]
    ]

store_btns = [
    [InlineKeyboardButton(text = 'store 1', callback_data='store_1')],
    [InlineKeyboardButton(text = 'store 2', callback_data='store_2')],
    [InlineKeyboardButton(text = 'store 3', callback_data='store_3')],
    [InlineKeyboardButton(text = 'store 4', callback_data='store_4')]
]


menu_kb = ReplyKeyboardMarkup(keyboard=menu_btns)
city_kb = InlineKeyboardMarkup(inline_keyboard=city_btns)
store_kb = InlineKeyboardMarkup(inline_keyboard=store_btns) 


#menu = InlineKeyboardMarkup(inline_keyboard=menu)


# Create a new button dynamically
#inline_keyboard = InlineKeyboardMarkup(row_width=1)
#create_request.add(KeyboardButton('New Button', callback_data='create_request'))

exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Выйти в меню")]],resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = "Выйти в меню", callback_data="menu")]])