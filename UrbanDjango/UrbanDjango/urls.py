"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from UrbanDjango.task2 import views
from UrbanDjango.task2 import views
from ..task3 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('class_view/', views.ClassBasedView.as_view(), name='class_view'),
    path('function_view/', views.functionBasedView, name='function_view'),
    path('', views.main_view, name='main'),
    path('shop/', views.shop_view, name='shop'),
    path('cart/', views.cart_view, name='cart'),
]



