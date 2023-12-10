from django.contrib import admin
from .models import Basis, Category


@admin.register(Basis)
class BasisAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_title', 'time_create', 'is_published', 'category')
    list_display_links = ('id', 'post_title')
    ordering = ['time_create', 'post_title']
    list_editable = ['is_published', 'category']
    list_per_page = 10
    list_filter = ['category__name', 'is_published']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
