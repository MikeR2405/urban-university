import telebot
import os
from crud_functions import initiate_db, get_all_products

API_TOKEN = os.getenv('API_TOKEN')
bot = telebot.TeleBot(API_TOKEN)

# Инициализация базы данных и добавление продуктов
initiate_db()


def get_buying_list():
    products = get_all_products()
    return products  # Возвращаем список продуктов


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Используйте команду /products для получения списка продуктов.")


@bot.message_handler(commands=['products'])
def list_products(message):
    products = get_buying_list()

    for product in products:
        id, title, description, price, image_path = product
        # Отправляем информацию о продукте
        response = f"Название: {title} | Описание: {description} | Цена: {price}"
        bot.send_photo(message.chat.id, photo=open(image_path, 'rb'), caption=response)


if __name__ == '__main__':
    bot.polling()
