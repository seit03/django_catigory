from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=233,
                                     verbose_name='Жанры')

    related_name = models.ForeignKey(max_length=233,
                                     verbose_name='Теги')

    def __str__(self):
        return f'{self.category_name}'


class TVShow(models.Model):
    class Meta:
        verbose_name = 'Сериал'
        verbose_name_plural = 'Сериалы'
    title = models.CharField(max_length=233,
                             verbose_name='Название сериала')
    body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True,
                                        verbose_name='Дата создание')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Дата обновление')
    image = models.ImageField(upload_to='tv/')
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.TextField()
    shows = models.ForeignKey(TVShow,
                              on_delete=models.CASCADE,
                              related_name='comments')
