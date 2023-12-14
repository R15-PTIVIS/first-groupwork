# Generated by Django 3.2.21 on 2023-12-14 06:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('joulukortti', '0004_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]