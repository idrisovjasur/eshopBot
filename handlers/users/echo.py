from aiogram import types
from aiogram.types import CallbackQuery

from loader import dp


# Echo bot
@dp.callback_query_handler()
async def universal(call:CallbackQuery):
    await call.answer('Bu bo\'limga mahsulotlar qo\'shilmagan\nLavashlar bo\'limiga o\'ting!',show_alert=True)
