from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Gold


def index(request):
    gold24_price = Gold.objects.get(name='gold24').price
    gold21_price = Gold.objects.get(name='gold21').price
    gold18_price = Gold.objects.get(name='gold18').price

    context = {
        'gold24': gold24_price,
        'gold21': gold21_price,
        'gold18': gold18_price,

    }
    return render(request, 'index.html', context=context)
