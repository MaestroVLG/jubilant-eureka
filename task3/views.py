from django.shortcuts import render

# Главная страница
def home_view(request):
    return render(request, 'third_task/home.html')

# Страница магазина
def store_view(request):
    items = {
        "Игровая приставка": "Купить",
        "Игра 1": "Купить",
        "Игра 2": "Купить",
    }
    return render(request, 'third_task/store.html', {'items': items})

# Страница корзины
def cart_view(request):
    return render(request, 'third_task/cart.html')
