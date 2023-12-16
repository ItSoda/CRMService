from django.contrib import admin

from .models import Tg_Bot, News


@admin.register(Tg_Bot)
class TgAdmin(admin.ModelAdmin):
    list_display = ("user_id", "first_name", "created_date")
    fields = (
        "user_id",
        "first_name",
        "last_name",
        "username",
    )
    readonly_fields = ("created_date", "update_date")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("text",)
