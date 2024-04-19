from unicodedata import category
from django.core.paginator import Paginator
from django.shortcuts import render
from django.template import context

from menu.models import Dishs

def menu(request, slug):

    page = request.GET.get('page', 1)

    
    if slug == 'all':
        dishs = Dishs.objects.all()
    else:    
        dishs = Dishs.objects.filter(category__slug=slug)

    paginator = Paginator(dishs, 4)
    current_page = paginator.page(int(page))    

    context = {
        'title': 'Меню',
        'dishs': current_page,
        'slug_url': slug
    }
    return render(request, 'menu/menu.html', context)

def dish(request, slug):
    dish = Dishs.objects.get(slug = slug)

    context = {
        'dish': dish
    }

    return render(request, 'menu/dish.html', context)
