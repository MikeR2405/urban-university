from django.shortcuts import render, redirect
from .models import Buyer, Game

def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        balance = request.POST.get('balance')
        age = request.POST.get('age')

        # Проверка на существование пользователя
        if Buyer.objects.filter(name=name).exists():
            return render(request, 'registration.html', {
                'error': f'Пользователь с именем "{name}" уже существует.'
            })

        # Создание нового покупателя
        Buyer.objects.create(name=name, balance=balance, age=age)
        return redirect('product_list')

    # Получение всех существующих покупателей для отображения (если нужно)
    buyers = Buyer.objects.all()
    return render(request, 'registration.html', {'buyers': buyers})

def product_list(request):
    games = Game.objects.all()  # Получаем все игры
    return render(request, 'product_list.html', {'games': games})

def cart(request):
    return render(request, 'cart.html')
