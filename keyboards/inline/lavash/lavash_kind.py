from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
lavash_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Orginal lavash',callback_data='orginal_lavash'),
            InlineKeyboardButton(text='Orginal kichik lavash',callback_data='orginal_kichik_lavash'),
        ],
        [
            InlineKeyboardButton(text='Pishloqli lavash',callback_data='pishloqli_lavash'),
            InlineKeyboardButton(text='Pishloqli kichik lavash',callback_data='pishloqli_kichik_lavash'),
        ],

        [
            InlineKeyboardButton(text='⬅️ Ortga',callback_data='ortga'),
        ],
    ]
)