from django.shortcuts import render

def menu(request):
    return render(request, 'menu/menu.html')

def dish(request):
    return render(request, 'menu/dish.html')
