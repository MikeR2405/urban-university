import os
from aiogram import Bot, types, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

load_dotenv()
api = os.getenv('API_TOKEN')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # Создаем клавиатуру с текстовыми кнопками
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Рассчитать', 'Информация', 'Купить')
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

@dp.message_handler(lambda message: message.text == 'Купить')
async def get_buying_list(message: types.Message):
    product_descriptions = [
        "Название: Product1 | Описание: описание 1 | Цена: 100",
        "Название: Product2 | Описание: описание 2 | Цена: 200",
        "Название: Product3 | Описание: описание 3 | Цена: 300",
        "Название: Product4 | Описание: описание 4 | Цена: 400"
    ]

    image_folder = 'C:/Users/SONY/PycharmProjects/URBAN/module_14/files'
    image_filenames = ['1.png', '2.png', '3.png', '4.png']

    for description, image_filename in zip(product_descriptions, image_filenames):
        await message.answer(description)
        with open(os.path.join(image_folder, image_filename), 'rb') as photo:
            await message.answer_photo(photo)  # Отправляем изображение после описания inline_markup = InlineKeyboardMarkup()
    for i in range(1, 5):
        button = InlineKeyboardButton(f'Product{i}', callback_data='product_buying')
        inline_markup.add(button)

    await message.answer('Выберите продукт для покупки:', reply_markup=inline_markup)

@dp.callback_query_handler(lambda call: call.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer('Вы успешно приобрели продукт!')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
