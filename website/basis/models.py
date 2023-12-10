from django.db import models
from django.urls import reverse


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=1)


class Basis(models.Model):
    post_title = models.CharField(max_length=255, verbose_name="Заголовок")
    post_content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", default=None, blank=True, null=True, verbose_name="Фото")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Слаг")
    category = models.ForeignKey(
        'Category', on_delete=models.PROTECT, related_name='all_posts', verbose_name="Категории", null=True
    )
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published = models.BooleanField(default=True, verbose_name="Статус")

    objects = models.Manager()
    published = PublishManager()

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = "объект"
        verbose_name_plural = "Объекты"

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    class Meta:
        verbose_name = "категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_slug': self.slug})
