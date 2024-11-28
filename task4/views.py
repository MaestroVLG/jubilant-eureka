from django.shortcuts import render

# Главная страница
def home_view(request):
    return render(request, 'fourth_task/home.html')

# Страница магазина
def store_view(request):
    games = ["Atomic Heart", "Cyberpunk 2077"]
    return render(request, 'fourth_task/store.html', {'games': games})

# Страница корзины
def cart_view(request):
    return render(request, 'fourth_task/cart.html')
