import os

from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, ReplyKeyboardButton
from aiogram.types.inline_keyboard import InlineKeyboardMarkup, InlineKeyboardButton

from dotenv import load_dotenv

load_dotenv()
api = os.getenv('API_TOKEN')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = ReplyKeyboardButton('Рассчитать')
    button2 = ReplyKeyboardButton('Информация')
    markup.add(button1, button2)
    await message.answer('Выберите опцию:', reply_markup=markup)

@dp.message_handler(lambda message: message.text == 'Рассчитать')
async def main_menu(message: types.Message):
    inline_markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Рассчитать норму калорий', callback_data='calories')
    button2 = InlineKeyboardButton('Формулы расчёта', callback_data='formulas')
    inline_markup.add(button1, button2)
    await message.answer('Выберите опцию:', reply_markup=inline_markup)

@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer('Формула Миффлина-Сан Жеора: (10 × вес в кг) + (6,25 × рост в см) - (5 × возраст в годах) + 5')

@dp.callback_query_handler(lambda call: call.data == 'calories')
async def set_age(call: types.CallbackQuery):
    await call.message.answer('Введите ваш возраст:')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

