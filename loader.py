from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.sql import Database
from data import config
from aiogram.types import ContentType
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(path_to_db='data/main.db')

@dp.message_handler(content_types=ContentType.PHOTO)
async def phone___def(message:types.Message):
    await message.answer(text=message.photo[-1].file_id)

