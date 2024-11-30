# task1/urls.py
from django.urls import path
from .views import index, product_list, cart, registration  # Замените index на Main

urlpatterns = [
    path('', index, name='home'),  # Главная страница
    path('products/', product_list, name='product_list'),  # Список товаров
    path('cart/', cart, name='cart'),  # Корзина
    path('register/', registration, name='registration'),  # Регистрация
]
