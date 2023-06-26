from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


menu = [
    [InlineKeyboardButton(text='Создать', callback_data="create_request"),
    InlineKeyboardButton(text='Меню', callback_data="menu")],
    [InlineKeyboardButton(text='Обновление', callback_data="refresh"),
    InlineKeyboardButton(text='Фильтр', callback_data="filter")],
    [InlineKeyboardButton(text='Открыть', callback_data="open")],
]


menu = InlineKeyboardMarkup(inline_keyboard=menu)


# Create a new button dynamically
#inline_keyboard = InlineKeyboardMarkup(row_width=1)
#create_request.add(KeyboardButton('New Button', callback_data='create_request'))

exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Выйти в меню")]],resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text = "Выйти в меню", callback_data="menu")]])