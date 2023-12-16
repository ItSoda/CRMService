from django.contrib import admin

from .models import EmailVerifications, Users, Roles


class EmailVerificationAdmin(admin.TabularInline):
    model = EmailVerifications
    fields = ("expiration",)
    extra = 0


@admin.register(Roles)
class RolesAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name")
    inlines = (EmailVerificationAdmin, )
    readonly_fields = ("last_login", "date_joined")
    filter_horizontal = ["roles"]