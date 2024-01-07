from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Ad(models.Model):
    image = models.ImageField(upload_to='ads/', verbose_name='image', default=None)
    title = models.CharField(max_length=100, verbose_name='title')
    price = models.IntegerField(verbose_name='price')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='user')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    description = models.TextField(verbose_name='description')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Comment(models.Model):
    text = models.TextField(verbose_name='text')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='user')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, **NULLABLE, verbose_name='advert')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
