from django.shortcuts import render, redirect

def main_view(request):
    return render(request, 'third_task/main.html')

def shop_view(request):
    shop_items = {
        "Игра 1": "Описание игры 1",
        "Игра 2": "Описание игры 2",
        "Игра 3": "Описание игры 3",
    }
    return render(request, 'third_task/shop.html', {'shop_items': shop_items})

def cart_view(request):
    return render(request, 'third_task/cart.html')