from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Маршрут для главной страницы
    path('posts/', views.post_list, name='post_list'),  # Маршрут для списка постов
]