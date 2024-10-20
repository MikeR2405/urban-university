import telebot
from telebot import types
from telebot.handler_backends import State, StatesGroup
from crud_functions import initiate_db, add_user, is_included
import os

# Инициализация базы данных
initiate_db()

# Инициализация бота
API_TOKEN = '8036900994:AAEudiZGeCebtbJ_z6FLXBkygUie5zKFvoI'
bot = telebot.TeleBot(API_TOKEN)


# Определение состояний
class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


# Команда для начала регистрации
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    registration_button = types.KeyboardButton("Регистрация")
    markup.add(registration_button)
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите действие:", reply_markup=markup)


# Обработка нажатия кнопки "Регистрация"
@bot.message_handler(func=lambda message: message.text == "Регистрация")
def sing_up(message):
    bot.send_message(message.chat.id, "Введите имя пользователя (только латинский алфавит):")
    bot.set_state(message.from_user.id, RegistrationState.username)


# Установка имени пользователя
@bot.message_handler(state=RegistrationState.username)
def set_username(message):
    username = message.text
    if not is_included(username):
        bot.user_data[message.from_user.id] = {'username': username}
        bot.set_state(message.from_user.id, RegistrationState.email)
        bot.send_message(message.chat.id, "Введите свой email:")
    else:
        bot.send_message(message.chat.id, "Пользователь существует, введите другое имя.")
        bot.set_state(message.from_user.id, RegistrationState.username)


# Установка email
@bot.message_handler(state=RegistrationState.email)
def set_email(message):
    email = message.text
    bot.user_data[message.from_user.id]['email'] = email
    bot.set_state(message.from_user.id, RegistrationState.age)
    bot.send_message(message.chat.id, "Введите свой возраст:")


# Установка возраста и добавление пользователя в БД
@bot.message_handler(state=RegistrationState.age)
def set_age(message):
    age = int(message.text)
    username = bot.user_data[message.from_user.id]['username']
    email = bot.user_data[message.from_user.id]['email']

    add_user(username, email, age)  # Добавляем пользователя в базу данных

    bot.send_message(message.chat.id, "Регистрация завершена! Добро пожаловать!")
    bot.finish_state(message.from_user.id)


# Запуск бота
bot.polling()
