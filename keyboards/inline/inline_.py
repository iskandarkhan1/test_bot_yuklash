from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

menu1 = InlineKeyboardMarkup (row_width=2)


menu1.insert(InlineKeyboardButton(text="Ha", callback_data="Ha"))  

menu1.insert(InlineKeyboardButton(text="Yo'q", callback_data= "xato "))