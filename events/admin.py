from django.contrib import admin
from .models import Events, Tags, Reviews

@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ["participants", "winners", "tags"]


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("event",)
