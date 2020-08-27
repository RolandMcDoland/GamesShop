from django.shortcuts import render
from .models import Offer

def home(request):
    context = { 'offers': Offer.objects.all() }
    return render(request, 'shop/home.html', context)
