from django.db import models

# Create your models here.
from django.db.models import Count


class Option(models.Model):
    name = models.CharField(max_length=50)
    value = models.BooleanField(default=False)


class Push(models.Model):
    class Meta:
        verbose_name_plural = 'Pushes'

    title = models.CharField(max_length=50)
    text = models.TextField()
    create_date = models.DateField()
    send_date = models.DateField()
    is_sent = models.BooleanField(default=False)
    objects = models.Manager()

    @property
    def count(self):
        return Push.objects.filter(is_sent=True).count()
