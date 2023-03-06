from aiogram import types
from aiogram.types import ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Regexp
from data.sms_function import send_sms_user
from keyboards.inline.menu_keyboard import menu_keyboard
from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state: FSMContext):
    users = db.select_all_users()
    id = []
    for user in users:
        id.append(user[0])
    if message.from_user.id in id:
        file = 'AgACAgIAAxkBAAMdY2-kz-jHiwWOfar_KMghK9resTYAAou_MRuihXhLTVz1l3nQPuEBAAMCAAN5AAMrBA'
        await message.answer_photo(file,
                                   caption='<b>Yetkazib berish bo\'limi Toshkent shaxrida soat 10:00 dan 3:00 gacha ishlaydi.</b>',
                                   reply_markup=menu_keyboard)


    else:
        msg = 'Ro\'yxatdan o\'tish uchun telefon raqamingizni kiriting\n\nRaqamni 998***** shaklida yuboring.'
        await message.answer(msg)
        await state.set_state('phone')


phone_regex = '^[\]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'


@dp.message_handler(Regexp(phone_regex), state='phone')
async def verify_phone(message: types.Message, state: FSMContext):
    phone = message.text
    code = send_sms_user(phone)
    await state.update_data(
        {
            'code': code,
            'phone': phone,
        }
    )
    await message.answer('Telefon raqamingizga yuborilgan tasdiqlash kodini kiriting.')
    await state.set_state('verify')
@dp.message_handler(state='phone')
async def verify_phone(message: types.Message, state: FSMContext):
    await message.answer('Namunada ko\'rstailgandek telefon raqam kiriting!\n\n'
                         'Misol uchun: 998991234567')

@dp.message_handler(state='verify')
async def verify(message: types.Message, state: FSMContext):
    text = message.text
    data = await state.get_data()
    code = data.get('code')
    phone = data.get('phone')
    if code == text:
        db.add_user(
            id=message.from_user.id,
            name=message.from_user.full_name,
            phone=phone
        )
        msg = f"{message.from_user.full_name}\n" \
              f"{message.from_user.id}\n" \
              f"{message.from_user.username}\n" \
              f"{phone} keldi!!!"
        await bot.send_message(chat_id=ADMINS[0], text=msg)
        await message.answer('Muaffaqiyatli ro\'yxatdan o\'tdngiz!!')
        file = 'AgACAgIAAxkBAAMdY2-kz-jHiwWOfar_KMghK9resTYAAou_MRuihXhLTVz1l3nQPuEBAAMCAAN5AAMrBA'
        await message.answer_photo(file,
                                   caption='<b>Yetkazib berish bo\'limi Toshkent shaxrida soat 10:00 dan 3:00 gacha ishlaydi.</b>',
                                   reply_markup=menu_keyboard)
    else:
        msg = 'Ro\'yxatdan o\'tish uchun telefon raqamingizni kiriting\n\nRaqamni 998***** shaklida yuboring.'
        await message.answer('Xatolik yuz berdi,tasdiqlash amalga oshirlmadi\n\n' +
                             msg)
        await state.finish()
