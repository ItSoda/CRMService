from django.contrib import admin
from .models import Events, Tags, Reviews, Teams

@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Events)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ["participian", "winners", "tags", "teams"]

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("event",)

@admin.register(Teams)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
    filter_horizontal = ["members"]
