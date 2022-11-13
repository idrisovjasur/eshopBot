import asyncio
import pyqrcode
from aiogram.types import ContentType
from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.types import Message,ReplyKeyboardRemove
from keyboards.default.contact import location
from keyboards.inline.lavash.lavash_kind import lavash_menu
from keyboards.inline.menu_keyboard import menu_keyboard, check_box,buying,order
from loader import dp,db


@dp.callback_query_handler(text='lavash')
async def lavash_main(call:CallbackQuery,state:FSMContext):
    file = 'AgACAgIAAxkBAAMkY2-lEmXZgTAaN4PslS7Q42FhXEkAAoy_MRuihXhLerCeGCIy2PUBAAMCAAN5AAMrBA'
    await call.message.delete()
    await call.message.answer_photo(file, caption='<b>Birini Tanlang!</b>', reply_markup=lavash_menu)

@dp.callback_query_handler(text='tarix')
async def tarix_def(call:CallbackQuery,state:FSMContext):
    product_list = db.select_product(id=call.from_user.id)
    if len(product_list)==0:
        await call.answer('Buyurtmalar tarixi mavjud emas!',show_alert=True)

    elif product_list!=None:
        await call.message.delete()
        msg=''
        for i in product_list:
            msg+=f"<b>Mahsulot nomi: {i[2]}\n" \
                 f"Mahsulot narxi: {i[4]}\n" \
                 f"Mahsulot soni: {i[3]} ta\n\n" \
                 f"{i[3]}*{i[4]}={i[3]*i[4]} so'm\n</b>" \
                 f"<i>\n------------------------------------------------\n</i>"
        await call.message.answer(text=msg,reply_markup=check_box)

@dp.callback_query_handler(text='delete_history')
async def delete_history_product(call:CallbackQuery,state:FSMContext):
    db.delete_product(id=call.from_user.id)
    await call.answer('Buyurtmalar tarixi tozalandi!',show_alert=True)
    await call.message.answer(text='<b>Davom etamizmi? ☺</b>️',reply_markup=menu_keyboard)

@dp.callback_query_handler(text='buyurtma')
async def buy_history_product(call:CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer(text='<b>Davom etamizmi? ☺</b>️',reply_markup=menu_keyboard)
#
@dp.callback_query_handler(text = 'savatcha')
async def tarix_def(call:CallbackQuery,state:FSMContext):
    product_list = db.select_product(id=call.from_user.id)
    if len(product_list)==0:
        await call.answer('🤷🏽‍♂️ Savatcha bo\'m bo\'sh!',show_alert=True)

    elif product_list!=None:
        await call.message.delete()
        s=0
        msg=''
        for i in product_list:
            msg+=f"<b>{i[2]}\n" \
                 f"└ {i[2]}</b> {i[3]}x{i[4]} = {i[3]*i[4]} so'm\n\n"
            s+=i[3]*i[4]
        await call.message.answer(text=msg+'\n'+f'Umumiy to\'lanadigan pul miqdori :{s} so\'m',reply_markup=buying)

############order

@dp.callback_query_handler(text='enter_buy')
async def buy_history_product(call:CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer(text='Yetkazib berish usulini tanlang️',reply_markup=order)
@dp.callback_query_handler(text='order_you')
@dp.callback_query_handler(text='order_we')
async def buy_history_product(call:CallbackQuery,state:FSMContext):
    await call.message.delete()
    msg='Iltimos, “📍 Geolokatsiyani jo’natish”' \
        'tugmasini bosish orqali geolokatsiyangizni yuboring. ' \
        'Bunda telefoningizda manzilni aniqlash funksiyasi yoqilgan' \
        ' bo’lishi lozim.'
    await call.message.answer(text=msg,reply_markup=location)
import os
@dp.message_handler(content_types=ContentType.LOCATION)
async def order_buying(message:Message):
    await message.answer('Kuting.....',reply_markup=ReplyKeyboardRemove())
    await asyncio.sleep(4)
    text = pyqrcode.create('8600312926661675', error='L')
    text.png('code.png', scale=10)
    await message.answer_photo(photo=open('code.png', 'rb'),caption='<b>QrCode\n'
                                                                    'Karta Raqam\n'
                                                                    ' └ 8600312926661675</b>\n\n'
                                                                    'To\'lov qiling!')
    os.remove('code.png')



