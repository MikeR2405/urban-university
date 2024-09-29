import os
from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()
api = os.getenv('API_TOKEN')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(text=['Urban', 'ff'])
async def urban_message(message):
    print("Urban message")
    await message.answer('Urban message')


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

    print('Start message')


@dp.message_handler()
async def all_message(message: types.Message):
    await message.answer(message.text)
    # await message.answer('Введите команду /start, чтобы начать общение.')
    print("Мы получили сообщение!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
