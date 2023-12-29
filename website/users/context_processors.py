from basis.views import get_menu
from basis.models import Category, Basis


def get_menu_context(request):
    return {'menu': get_menu()}


def get_categories():
    return Category.objects.all()


def get_basis_creation(**kwargs):
    return Basis.objects.create(**kwargs)


def get_basis_model():
    return Basis
