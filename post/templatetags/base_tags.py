from django import template
from ..models import Category


register = template.Library()

@register.inclusion_tag('blog/partials/category_nav.html')
def CATEGORY():
    return {
        'category':Category.objects.active_category()
    }