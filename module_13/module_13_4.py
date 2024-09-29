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
    adress = State()
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Calories')
async def set_age(message: types.Message):
    await message.answer("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: UserState):
    await state.update_data(age=int(message.text))
    await message.answer("Введите свой рост:")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: UserState):
    await state.update_data(growth=int(message.text))
    await message.answer("Введите свой вес:")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def set_calories(message: types.Message, state: UserState):
    await state.update_data(weight=int(message.text))
    data = await state.get_data()
    age = data['age']
    growth = data['growth']
    weight = data['weight']
    calories = 10 * weight + 6.25 * growth - 5 * age - 161
    await message.answer(f'Ваша дневная норма каллории: {calories:.2f} ккал')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
