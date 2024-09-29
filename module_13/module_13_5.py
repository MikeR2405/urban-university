import os
from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from dotenv import load_dotenv

load_dotenv()
api = os.getenv('API_TOKEN')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton('Рассчитать'), types.KeyboardButton('Информация'))
    await message.answer('Выберите действие:', reply_markup=markup)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def set_age(message: types.Message):
    await UserState.age.set()
    await message.answer('Введите свой возраст:')

@dp.message_handler(state=UserState.age)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = int(message.text)
    await UserState.next()
    await message.answer('Введите свой рост:')

@dp.message_handler(state=UserState.growth)
async def process_growth(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['growth'] = int(message.text)
    await UserState.next()
    await message.answer('Введите свой вес:')

@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['weight'] = int(message.text)
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    # Simplified Mifflin-St. Jeor equation for women
    calories = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f'Ваша дневная норма калорий: {calories:.2f} ккал')
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
