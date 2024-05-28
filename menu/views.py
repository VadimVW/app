from unicodedata import category
from django.core.paginator import Paginator
from django.shortcuts import render
from django.template import context

from menu.models import Dishs
from menu.utils import q_search

def menu(request, slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by  = request.GET.get('order_by', None)
    query  = request.GET.get('q', None)


    if slug == 'all':
        dishs = Dishs.objects.all()
    elif query or query == '':
        dishs = q_search(query)
    else:    
        dishs = Dishs.objects.filter(category__slug=slug)

    if on_sale:
        dishs = dishs.filter(discount__gt=0)
        
    if order_by and order_by != "default":
        dishs = dishs.order_by(order_by)



    paginator = Paginator(dishs, 8)
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
