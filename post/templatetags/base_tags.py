from django import template
from ..models import Category


register = template.Library()

@register.inclusion_tag('blog/partials/navbar.html')
def Navbar():
    return {
        'category':Category.objects.active_category()
    }