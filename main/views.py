from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render

from menu.models import Categories

def index(request):

    context = {
        'title': 'Головна',
        'content': 'Замовити їжу',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Про нас',
        'content': 'Про нас...',

    }
    return render(request, 'main/about.html', context)