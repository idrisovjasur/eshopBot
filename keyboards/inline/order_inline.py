from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

def build_keyboard(product):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            InlineKeyboardButton(text='Xarid Qilish',callback_data=f"product:{product}")
        ],
    )

    return keyboard