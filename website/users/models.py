from django.db import models
from django.contrib.auth.models import AbstractUser


class UploadFiles(models.Model):
    file = models.FileField(upload_to='upload_files')


class User(AbstractUser):
    photo = models.ImageField(upload_to="users/%Y/%m/%d/", blank=True, null=True, verbose_name="Фотография")
    first_name = models.TextField(blank=True, null=True, verbose_name="Имя")
    last_name = models.TextField(blank=True, null=True, verbose_name="Фамилия")
    date_birth = models.DateTimeField(blank=True, null=True, verbose_name="Дата рождения")
