from aiogram.types import KeyboardButton, ReplyKeyboardMarkup ,ReplyKeyboardRemove


menu = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)


menu.insert(KeyboardButton("Sherik kerak"))  

menu.insert(KeyboardButton("Hodim kerak"))

menu.insert(KeyboardButton("Ish-joy kerak"))

menu.insert(KeyboardButton("Uztoz kerak"))

menu.insert(KeyboardButton("Shogirt kerak"))




tugri = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)

tugri.insert(KeyboardButton("Ha"))
tugri.insert(KeyboardButton("Yo'q"))

tugri1 = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)

tugri1.insert(KeyboardButton("Orqaga"))






