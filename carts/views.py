from urllib import response
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from carts.models import Cart
from carts.utils import get_user_carts
from menu.models import Dishs


def cart_add(request):


    product_id = request.POST.get("product_id")
    dish = Dishs.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, dish=dish)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, dish=dish, quantity=1)  

    
    user_cart = get_user_carts(request)
    cart_items_html = render_to_string(
        "carts/includes/included_carts.html", {"carts": user_cart}, request=request
    )     

    response_data = {
        "message": "Страва додана у кошик",
        "cart_items_html": cart_items_html,
    }

    return JsonResponse(response_data)


def cart_change(request, product_slug):
    ...

def cart_remove(request):
    ...
    # cart = Cart.objects.get(id=cart_id)
    # cart.delete()

    # return redirect(request.META['HTTP_REFERER'])  
