from aiogram import types
from aiogram.types import ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart,Regexp

from keyboards.inline.menu_keyboard import menu_keyboard
from loader import dp,db

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message,state:FSMContext):
    users = db.select_all_users()
    id = []
    for user in users:
        id.append(user[0])
    if message.from_user.id in id:
        file = 'AgACAgIAAxkBAAMdY2-kz-jHiwWOfar_KMghK9resTYAAou_MRuihXhLTVz1l3nQPuEBAAMCAAN5AAMrBA'
        await message.answer_photo(file,
                                   caption='<b>Yetkazib berish bo\'limi Toshkent shaxrida soat 10:00 dan 3:00 gacha ishlaydi.</b>',
                                   reply_markup=menu_keyboard)
        # await message.answer('siz borsz')
    else:
       msg='Ro\'yxatdan o\'tish uchun telefon raqamingizni kiriting\n\nRaqamni +998***** shaklida yuboring.'
       await message.answer(msg)
       await state.set_state('phone')





@dp.message_handler(Regexp('^\+[1-9]\d{1,18}$'),state='phone')
async def phone(message:types.Message,state:FSMContext):
    phone = message.text
    await state.update_data(
        {
            'phone':phone
        }
    )
    data = await state.get_data()
    phone = data.get('phone')
    await state.finish()
    db.add_user(
            id=message.from_user.id,
            name=message.from_user.full_name,
            phone=phone
        )
    file = 'AgACAgIAAxkBAAMdY2-kz-jHiwWOfar_KMghK9resTYAAou_MRuihXhLTVz1l3nQPuEBAAMCAAN5AAMrBA'
    await message.answer_photo(file,
                                   caption='<b>Yetkazib berish bo\'limi Toshkent shaxrida soat 10:00 dan 3:00 gacha ishlaydi.</b>',
                                   reply_markup=menu_keyboard)


