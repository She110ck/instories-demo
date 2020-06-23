from django.db import models

# Create your models here.
from django.db.models import Count


class Option(models.Model):
    name = models.CharField(max_length=50)
    value = models.BooleanField(default=False)


# @admin_thumbnails.thumbnail('image')
class Push(models.Model):
    class Meta:
        verbose_name_plural = 'Pushes'

    def __str__(self):
        return self.title

    title = models.CharField(max_length=50, null=True, blank=True, verbose_name=' Укажите заголовок')
    text = models.TextField(null=True, blank=True, verbose_name='Текст уведомления')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение уведомления')
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Название уведомления')
    create_date = models.DateField(null=True, blank=True, auto_now=True)
    send_date = models.DateField(null=True, blank=True, verbose_name='Дата отправки')
    is_sent = models.BooleanField(null=True, blank=True, default=False, verbose_name='Отправлен')

    @property
    def count(self):
        return Push.objects.filter(is_sent=True).count()
