from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton("/Режим Работы")
b2 = KeyboardButton("/Расположение")
b3 = KeyboardButton("/Меню")
b4 = KeyboardButton("поделится номером", request_contact=True)
b5 = KeyboardButton("отправить где я", request_location=True )

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).insert(b3).row(b4, b5)

