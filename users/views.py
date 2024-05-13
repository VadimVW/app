from django.shortcuts import render


def login(request):
    context = {
        'title': 'Авторизація'
    }
    return render(request, 'users/login.html', context)


def registration(request):
    context = {
        'title': 'Регістрація'
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'Особистий кабінет'
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...