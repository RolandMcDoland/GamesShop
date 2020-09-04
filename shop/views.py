from django.shortcuts import render, redirect
from .models import Offer

def home(request):
    context = { 'offers': Offer.objects.all() }
    return render(request, 'shop/shop.html', context)

def cart(request):
    context = { 'offers': Offer.objects.filter(in_order = True) }

    sum = 0
    for offer in context['offers']:
        sum += offer.price
    context['total'] = sum

    return render(request, 'shop/cart.html', context)

def add_to_cart(request, name):
    offer_to_update = Offer.objects.get(name = name)
    offer_to_update.in_order = True
    offer_to_update.save()
    return redirect('shop-home')

def remove_from_cart(request, name):
    offer_to_update = Offer.objects.get(name = name)
    offer_to_update.in_order = False
    offer_to_update.save()
    return redirect('shop-cart')