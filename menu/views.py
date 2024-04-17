from django.shortcuts import render
from django.template import context

def menu(request):
    context = {
        'title': 'Меню',
        'goods': [
        {'image': 'deps/images/goods/BBQ pizza.png',
         'name': 'Чайный столик и три стула',
         'description': 'Комплект из трёх стульев и дизайнерский столик для гостинной комнаты.',
         'price': 150.00},

         {'image': 'deps/images/goods/pizza noname.png',
         'name': 'Чайный столик и два стула',
         'description': 'Набор из стола и двух стульев в минималистическом стиле.',
         'price': 93.00},

         {'image': 'deps/images/goods/meat pizza.png',
         'name': 'Двухспальная кровать',
         'description': 'Кровать двухспальная с надголовником и вообще очень ортопедичная.',
         'price': 670.00},

         {'image': 'deps/images/goods/Chicago pizza.png',
         'name': 'Кухонный стол с раковиной',
         'description': 'Кухонный стол для обеда с встроенной раковиной и стульями.',
         'price': 365.00},

         {'image': 'deps/images/goods/Pepperoni pizza.png',
         'name': 'Кухонный стол с встройкой',
         'description': 'Кухонный стол со встроенной плитой и раковиной. Много полок и вообще красивый.',
         'price': 430.00},

         {'image': 'deps/images/goods/pizza four cheeses.png',
         'name': 'Угловой диван для гостинной',
         'description': 'Угловой диван, раскладывается в двухспальную кровать, для гостинной и приема гостей самое то!',
         'price': 610.00},

         {'image': 'deps/images/goods/pizza Frutti de Mare.png',
         'name': 'Прикроватный столик',
         'description': 'Прикроватный столик с двумя выдвижными ящиками (цветок не входит в комплект).',
         'price': 55.00},

         {'image': 'deps/images/goods/pizza margarita.png',
         'name': 'Диван обыкновенный',
         'description': 'Диван, он же софа обыкновенная, ничего примечательного для описания.',
         'price': 190.00},

         {'image': 'deps/images/goods/pizza noname.png',
         'name': 'Стул офисный',
         'description': 'Описание товара, про то какой он классный, но это стул, что тут сказать...',
         'price': 30.00},

         {'image': 'deps/images/goods/pizza with chicken and pineapples.png',
         'name': 'Растение',
         'description': 'Растение для украшения вашего интерьера подарит свежесть и безмятежность обстановке.',
         'price': 10.00},

         {'image': 'deps/images/goods/flower.jpg',
         'name': 'Цветок стилизированный',
         'description': 'Дизайнерский цветок (возможно искусственный) для украшения интерьера.',
         'price': 15.00},

         {'image': 'deps/images/goods/strange table.jpg',
         'name': 'Прикроватный столик',
         'description': 'Столик, довольно странный на вид, но подходит для размещения рядом с кроватью.',
         'price': 25.00},
        ]

    }
    return render(request, 'menu/menu.html', context)

def dish(request):
    return render(request, 'menu/dish.html')
