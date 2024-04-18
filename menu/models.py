from email.mime import image
from tabnanny import verbose
from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.name


class Dishs(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Опис')
    image = models.ImageField(blank=True, null=True, upload_to='menu_images', verbose_name='Зображення')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Ціна')
    discount = models.IntegerField(default=0, verbose_name='Знижка у %')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категорія')

    class Meta:
        db_table = 'dish'
        verbose_name = 'Страву'
        verbose_name_plural = 'Страви'

    def __str__(self):
        return self.name
    
    def sell_price(self):
        return round(self.price - self.price * self.discount / 100, 2)