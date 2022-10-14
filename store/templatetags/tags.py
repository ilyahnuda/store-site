from django import template
from django.db.models import Count, F
from ..models import *
from django.core.cache import cache

register = template.Library()


@register.simple_tag
def get_all_products(user):
    if user.is_authenticated:
        customer = user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        carItems = order.get_cart_items
    else:
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        carItems = order['get_cart_items']
    return carItems
