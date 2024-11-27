from django.urls import path
from .views import home_view, store_view, cart_view

urlpatterns = [
    path('', home_view, name='home'),  #главная
    path('store/', store_view, name='store'),  #магазин
    path('cart/', cart_view, name='cart'), #корзина
]
