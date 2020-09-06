from django.shortcuts import render, redirect
from .models import Offer
from .authorization import auth_dict
import requests
import json

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

def order(request):
    return render(request, 'shop/order.html')

def payment(request):
    auth_response = requests.post("https://secure.snd.payu.com/pl/standard/user/oauth/authorize", data=auth_dict)
    auth_cred = json.loads(auth_response.text)

    items = Offer.objects.filter(in_order = True)

    sum = 0
    products = []

    for item in items:
        sum += item.price
        product = { 'name': item.name, 'unitPrice': str(int(item.price * 100)), 'quantity': '1' }
        products.append(product)

        item.in_order = False
        item.save()

    payment_dict = {
        "notifyUrl": "http://127.0.0.1:8000/",
        "customerIp": "127.0.0.1",
        "merchantPosId": "394143",
        "description": "Games shop",
        "currencyCode": "PLN",
        "totalAmount": str(int(sum * 100)),
        "continueUrl": "http://127.0.0.1:8000/cart/order/thanks",
        "buyer": {
            "email": request.POST.get("email"),
            "phone": request.POST.get("phone"),
            "firstName": request.POST.get("firstName"),
            "lastName": request.POST.get("lastName"),
            "language": "pl"
        },
        "settings":{
            "invoiceDisabled":"true"
        },
        "products": products
    }

    headers = {'Content-type': 'application/json', 'Authorization': 'Bearer ' + auth_cred['access_token']}

    payU_response = requests.post("https://secure.snd.payu.com/api/v2_1/orders", json=payment_dict, headers=headers, allow_redirects=False)

    return redirect(json.loads(payU_response.text)['redirectUri'])

def thanks(request):
    return render(request, 'shop/thanks.html')