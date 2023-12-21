from .models import Basis, Category
from django.contrib import admin, messages


@admin.register(Basis)
class BasisAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('post_title',)}
    list_display = ('id', 'post_title', 'time_create', 'is_published', 'category')
    list_display_links = ('id', 'post_title')
    ordering = ['time_create', 'post_title']
    list_editable = ['is_published', 'category']
    list_per_page = 10
    actions = ['set_published', 'set_draft']
    search_fields = ['post_title', 'category__name']
    list_filter = ['category__name', 'is_published']

    @admin.action(description="Опубликовать выбранные записи")
    def set_published(self, request, queryset):
        counter = queryset.update(is_published=Basis.Status.PUBLISHED)
        self.message_user(request, f"Изменено {counter} записей")

    @admin.action(description="Снять с публикации выбранные записи")
    def set_draft(self, request, queryset):
        counter = queryset.update(is_published=Basis.Status.DRAFT)
        self.message_user(request, f"{counter} записей снято с публикации", messages.WARNING)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
