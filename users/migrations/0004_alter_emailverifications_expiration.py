# Generated by Django 4.2 on 2023-12-16 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_create_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifications',
            name='expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]