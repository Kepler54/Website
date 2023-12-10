from django import template
from basis.models import Category

register = template.Library()


@register.inclusion_tag('basis/categories.html')
def get_categories(category_selected=0):
    categories = Category.objects.all()
    return {'categories': categories, 'category_selected': category_selected}
