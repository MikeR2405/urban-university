from django.shortcuts import render, redirect

def main_view(request):
    return render(request, 'fourth_task/main.html')

def shop_view(request):
    shop_items = [
        "Atomic Heart",
        "Cyberpunk 2077"
    ]
    return render(request, 'fourth_task/shop.html', {'shop_items': shop_items})

def cart_view(request):
    return render(request, 'fourth_task/cart.html')