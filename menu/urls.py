from django.urls import path

from menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu, name='index'),
    path('dish/<slug:slug>', views.dish, name='dish'),
]
