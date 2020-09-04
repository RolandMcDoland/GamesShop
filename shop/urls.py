from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='shop-home'),
    path('cart', views.cart, name='shop-cart'),
    path('cart/add/<str:name>/', views.add_to_cart),
    path('cart/remove/<str:name>/', views.remove_from_cart),
]
