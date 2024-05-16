from os import name
from django import template
from django.utils.http import urlencode
from django.db.models import Case, When

from menu.models import Categories


register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag()
def tag_sorted_categories():
    return Categories.objects.annotate(
    is_all_goods=Case(
        When(name__contains="Всі товари", then=0),
        default=1,
    )
).order_by('is_all_goods')

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
