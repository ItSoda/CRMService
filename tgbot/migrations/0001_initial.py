# Generated by Django 4.2 on 2023-12-16 15:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="news_bot_images"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tg_Bot",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_id", models.IntegerField(unique=True, verbose_name="USER ID")),
                ("username", models.CharField(blank=True, max_length=256, null=True)),
                ("first_name", models.CharField(max_length=256, verbose_name="Name")),
                ("last_name", models.CharField(blank=True, max_length=256, null=True)),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("update_date", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
