from django.shortcuts import get_object_or_404
from shop.models import Shop
from django import template
register = template.Library()
@register.simple_tag
def greet(user):
    try:
        if user.is_authenticated:
            shop_exists = get_object_or_404(Shop, created_by=user)
            return shop_exists
    except:
        pass
    return False