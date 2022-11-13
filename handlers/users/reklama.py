from aiogram.types import Message
from loader import dp,bot,db
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
import asyncio
@dp.message_handler(text ='reklama',user_id = ADMINS)
async def reklama_def(message:Message,state:FSMContext):
    await state.set_state('reklama')
    await message.answer('Captionni Yuboring!')
@dp.message_handler(state = 'reklama')
async def reklama_state_def(message:Message,state:FSMContext):
    text = message.text
    users = db.select_all_users()
    await state.finish()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id = user_id,text=text)
        await asyncio.sleep(0.5)





