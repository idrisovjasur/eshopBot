from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

location = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📍 Geolokatsiyani jo’natish',request_location=True),
        ],
    ],resize_keyboard=True,
)

db_save = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='✅ Ha'),
            KeyboardButton(text='❌ Yo\'q')
        ],
    ],resize_keyboard=True
)


