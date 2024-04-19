from unicodedata import category
from django.shortcuts import render
from django.template import context

from menu.models import Dishs

def menu(request, slug):
    
    if slug == 'all':
        dishs = Dishs.objects.all()
    else:    
        dishs = Dishs.objects.filter(category__slug=slug)

    context = {
        'title': 'Меню',
        'dishs': dishs,
    }
    return render(request, 'menu/menu.html', context)

def dish(request, slug):
    dish = Dishs.objects.get(slug = slug)

    context = {
        'dish': dish
    }

    return render(request, 'menu/dish.html', context)
