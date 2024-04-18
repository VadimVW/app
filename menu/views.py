from django.shortcuts import render
from django.template import context

from menu.models import Dishs

def menu(request):

    dishs = Dishs.objects.all()

    context = {
        'title': 'Меню',
        'dishs': dishs,
    }
    return render(request, 'menu/menu.html', context)

def dish(request):
    return render(request, 'menu/dish.html')
