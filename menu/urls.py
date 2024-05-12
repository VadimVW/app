from django.urls import path

from menu import views

app_name = 'menu'

urlpatterns = [
    path('search/', views.menu, name='search'),
    path('<slug:slug>', views.menu, name='index'),
    path('dish/<slug:slug>', views.dish, name='dish'),
]
