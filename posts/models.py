from categories.models import Category
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Titulo')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Autor')
    date = models.DateTimeField(default=timezone.now, verbose_name='Data')
    content = models.TextField()
    content_excerpt = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name='Categoria')
    image = models.ImageField(
        upload_to='post_image/%Y/%m/%d', blank=True, null=True)
    publish = models.BooleanField(default=False, verbose_name='Publicado')

    def __str__(self):
        return self.title
