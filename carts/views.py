from django.shortcuts import redirect, render

from carts.models import Cart
from menu.models import Dishs


def cart_add(request, dish_slug):
    
    dish = Dishs.objects.get(slug=dish_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, dish=dish)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, dish=dish, quantity=1)  

    return redirect(request.META['HTTP_REFERER'])      


def cart_change(request, product_slug):
    ...

def cart_remove(request, product_slug):
    ...
