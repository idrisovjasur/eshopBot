from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery, Message
from data.config import ADMINS
from keyboards.inline.order_inline import build_keyboard
from loader import dp, bot
from data.products import orginal_lavash, orginal_kichik_lavash,  FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING



@dp.message_handler(Command("orginal"))
async def show_invoices(message: types.Message):
    caption = 'Orginal Lavash'
    await message.answer(text=caption, reply_markup=build_keyboard("orginal_lavash"))

@dp.message_handler(Command("kichik"))
async def show_invoices(message: types.Message):
    caption = 'Orginal Kichik Lavash Mazzali'

    await message.answer_photo(photo="https://i.imgur.com/vRN7PBT.jpg",
                         caption=caption, reply_markup=build_keyboard("orginal_kichik_lavash"))

# @dp.message_handler(Command("mahsulotlar"))
# async def book_invoice(message: Message):
#     await bot.send_invoice(chat_id=message.from_user.id,
#                            **python_book.generate_invoice(),
#                            payload="123456")
#     await bot.send_invoice(chat_id=message.from_user.id,
#                            **ds_praktikum.generate_invoice(),
#                            payload="123457")

@dp.callback_query_handler(text="product:orginal_lavash")
async def book_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **orginal_lavash.generate_invoice(),
                           payload="payload:orginal_lavash")
    await call.answer()


@dp.callback_query_handler(text="product:orginal_kichik_lavash")
async def praktikum_invoice(call: CallbackQuery):
    await bot.send_invoice(chat_id=call.from_user.id,
                           **orginal_kichik_lavash.generate_invoice(),
                           payload="payload:orginal_kichik_lavash")
    await call.answer()


@dp.shipping_query_handler()
async def choose_shipping(query: types.ShippingQuery):
    if query.shipping_address.country_code != "UZ":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        ok=False,
                                        error_message="Chet elga yetkazib bera olmaymiz")
    elif query.shipping_address.city.lower() == "tashkent":
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[FAST_SHIPPING, REGULAR_SHIPPING, PICKUP_SHIPPING],
                                        ok=True)
    else:
        await bot.answer_shipping_query(shipping_query_id=query.id,
                                        shipping_options=[REGULAR_SHIPPING],
                                        ok=True)


@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id,
                                        ok=True)
    await bot.send_message(chat_id=pre_checkout_query.from_user.id,
                           text="Xaridingiz uchun rahmat!")
    await bot.send_message(chat_id=ADMINS[0],
                           text=f"Quyidagi mahsulot sotildi: {pre_checkout_query.invoice_payload}\n"
                                f"ID: {pre_checkout_query.id}\n"
                                f"Telegram user: {pre_checkout_query.from_user.first_name}\n"                                
                                f"Xaridor: {pre_checkout_query.order_info.name}, tel: {pre_checkout_query.order_info.phone_number}")