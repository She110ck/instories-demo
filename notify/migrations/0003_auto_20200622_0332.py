# Generated by Django 2.2.12 on 2020-06-21 23:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notify', '0002_auto_20200622_0251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='push',
            options={'verbose_name_plural': 'Pushes'},
        ),
        migrations.AlterModelManagers(
            name='push',
            managers=[
            ],
        ),
    ]
