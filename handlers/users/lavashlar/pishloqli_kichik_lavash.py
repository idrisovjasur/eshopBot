from aiogram.types.callback_query import CallbackQuery
from aiogram.dispatcher import FSMContext
from keyboards.inline.keyboard_number import tanlanma_keyboard,list1
from keyboards.inline.lavash.lavash_kind import lavash_menu
from keyboards.inline.menu_keyboard import menu_keyboard
from loader import dp,db


@dp.callback_query_handler(text='pishloqli_kichik_lavash')
async def pishloqli_lavash(call:CallbackQuery,state:FSMContext):
     file = 'AgACAgIAAxkBAAIJMGNPy3_a5hyGkuzWgkDLuVPyDwPEAALqwTEbdWSASi3fObEqsjuuAQADAgADeQADKgQ'
     await call.message.answer_photo(file, caption='<b>Pishloqli kichik lavashm</b>\n\nNarxi:18000\n'
                                                   'Iltimos kerakli miqdorni kiriting!', reply_markup=tanlanma_keyboard(0))
     list1.pop()
     await state.set_state('pishloqli_kichik_lavash')
     await call.message.delete()

@dp.callback_query_handler(state='pishloqli_kichik_lavash')
async def orginal_lavash_state(call:CallbackQuery,state:FSMContext):
     data = call.data
     if len(list1)==0 and data=='joylash':
          await call.answer(text='Siz hech qancha mahsulot tanlamadingiz!',show_alert=True)
     elif data=='joylash' and len(list1)!=0:
          for i in list1:
               global y
               y = str()
               y+=i
          y = int(y)
          db.add_product(
                    id=call.from_user.id,
                    name=call.from_user.full_name,
                    productname='Pishloqli kichik lavash',
                    quantity=y,
                    price=18000
               )
          await call.answer("Buyurtmangiz qabul qilindi,davom etamizmi?",show_alert=True)
          file = 'AgACAgIAAxkBAAMaY0fwH5JoMlbLuFrAB9cWF_qyHGsAAk-_MRtq7UFK3AxrzMjwU-oBAAMCAAN5AAMqBA'
          await call.message.delete()
          await call.message.answer_photo(file, caption='<b>Birini Tanlang!</b>', reply_markup=menu_keyboard)
          await state.finish()
          list1.clear()
     elif call.data == 'orqaga':
         await call.message.delete()
         file = 'AgACAgIAAxkBAANUY0f7R3HyX0oOUBbkAAGTW6FJMu4EAAJ6vzEbau1BSl__-7qopCj9AQADAgADeQADKgQ'
         await call.message.answer_photo(file, caption='<b>Birini Tanlang!</b>', reply_markup=lavash_menu)
         list1.clear()
         await state.finish()

     else:
          await call.message.edit_reply_markup(reply_markup=tanlanma_keyboard(data))



