from django.db import models

from users.models import User
from menu.models import Dishs


class CartQueryset(models.QuerySet):
    
    def total_price(self):
        return sum(cart.dishs_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Cart(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Користувач')
    dish = models.ForeignKey(to=Dishs, on_delete=models.CASCADE, verbose_name='Cтрава')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Кількість')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Дата додання')

    class Meta:
        db_table = 'cart'
        verbose_name = "Кошик"
        verbose_name_plural = "Кошики"

    objects = CartQueryset().as_manager()

    def dishs_price(self):
        return round(self.dish.sell_price() * self.quantity, 2)

    def __str__(self):
        if self.user:
            return f'Кошик {self.user.username} | Cтрава {self.dish.name} | Кількість {self.quantity}'


        return f'Анонімний кошик | Cтрава {self.dish.name} | Кількість {self.quantity}'
