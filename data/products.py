from aiogram import types
from aiogram.types import LabeledPrice

from utils.misc.products import Product


orginal_lavash = Product(
    title="Orginal lavash",
    description="Orginal lavash narxi 25000 so'm",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='orginal_lavash',
            amount=25000, #150.00$
        )
    ],
    start_parameter="create_invoice_orginal_lavash",
    photo_url='https://i.imgur.com/vRN7PBT.jpg',
    photo_width=1280,
    photo_height=564,
    # photo_size=600,
    need_email=True,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True,
    is_flexible=True
)

orginal_kichik_lavash = Product(
    title="Orginal Kichik Lavash",
    description="Orginal Kichik lavash Narxi 22000 so'm",
    currency="UZS",
    prices=[
        LabeledPrice(
            label='orginal_kichik_lavash',
            amount=22000,#5.00$
        ),
        LabeledPrice(
            label='Yetkazib berish (1 soat)',
            amount=1000,#1.00$
        ),
    ],
    start_parameter="create_invoice_orginal_kichik_lavash",
    photo_url='https://i.imgur.com/0IvPPun.jpg',
    photo_width=851,
    photo_height=1280,
    # photo_size=800,
    need_name=True,
    need_phone_number=True,
    need_shipping_address=True, # foydalanuvchi manzilini kiritishi shart
    is_flexible=True,
)

REGULAR_SHIPPING = types.ShippingOption(
    id='post_reg',
    title="Fargo (0.5 soat)",
    prices=[
        LabeledPrice(
            'Maxsus quti', 100),
        LabeledPrice(
            '3 ish kunida yetkazish', 100),
    ]
)
FAST_SHIPPING = types.ShippingOption(
    id='post_fast',
    title='Express pochta (1 kun)',
    prices=[
        LabeledPrice(
            '1 kunda yetkazish', 100),
    ]
)

PICKUP_SHIPPING = types.ShippingOption(id='pickup',
                                       title="Do'kondan olib ketish",
                                       prices=[
                                           LabeledPrice("Yetkazib berishsiz", -100)
                                       ])