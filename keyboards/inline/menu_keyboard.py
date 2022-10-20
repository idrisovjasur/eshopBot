from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🌯 Lavashlar',callback_data='lavash'),
            InlineKeyboardButton(text='🍱 Setlar',callback_data='set'),
        ],
        [
            InlineKeyboardButton(text='🥙 Xaggi',callback_data='xaggi'),
            InlineKeyboardButton(text='🍰 Shirinliklar',callback_data='shirinlik'),
        ],
        [
            InlineKeyboardButton(text='🍕 Pitsalar',callback_data='pitsa'),
            InlineKeyboardButton(text='🥪 Klab Sendvich',callback_data='klab_sendvich'),
        ],
        [
            InlineKeyboardButton(text='🍔 Burger va Donerlar',callback_data='burger_doner'),
            InlineKeyboardButton(text='🌭 Hotdoglar',callback_data='hotdog'),
        ],
        [
            InlineKeyboardButton(text='🍟 Sneklar',callback_data='snek'),
            InlineKeyboardButton(text='🥗 Salatlar',callback_data='salat'),
        ],
        [
            InlineKeyboardButton(text='🧂 Ichimliklar',callback_data='ichimlik'),
            InlineKeyboardButton(text='🍅 Souslar',callback_data='sous'),
        ],
        [
            InlineKeyboardButton(text='📖 Buyurtmalar Tarixi',callback_data='tarix'),
        ],
        [
            InlineKeyboardButton(text='🛒 Savatchaga o\'tish',callback_data='savatcha'),
        ]
    ],
)

check_box = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='♻️ Tozalash',callback_data='delete_history')
        ],
        [
            InlineKeyboardButton(text='↩️ Menuga o\'tish',callback_data='buyurtma')
        ]
    ]
)

buying = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🧾 Buyurtmani tasdiqlash',callback_data='enter_buy')
        ],
        [
            InlineKeyboardButton(text='Yana buyurtma berish',callback_data='buyurtma')
        ]
    ]
)

order = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🚚 Yetkazib berish',callback_data='order_we'),
            InlineKeyboardButton(text='🏃‍♂️ Olib ketish', callback_data='order_you'),

        ],
        [
            InlineKeyboardButton(text='🔙 Ortga',callback_data='ortga')
        ],
    ],
)