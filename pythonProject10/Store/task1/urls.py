# task1/urls.py
from django.urls import path
from .views import Main, product_list, cart, registration  # Замените index на Main

urlpatterns = [
    path('', Main, name='home'),  # Главная страница
    path('products/', product_list, name='product_list'),  # Список товаров
    path('cart/', cart, name='cart'),  # Корзина
    path('register/', registration, name='registration'),  # Регистрация
]
