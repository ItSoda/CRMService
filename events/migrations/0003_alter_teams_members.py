# Generated by Django 4.2 on 2023-12-16 21:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teams',
            name='members',
            field=models.ManyToManyField(related_name='users_members', to=settings.AUTH_USER_MODEL),
        ),
    ]
