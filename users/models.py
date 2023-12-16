from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from users.services import is_expired, send_verification_email

from .managers import CustomUserManager


class Roles(models.Model):
    """Model for roles"""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "роль"
        verbose_name_plural = "роли"

    def __str__(self):
        return f"tags {self.name}"


class Users(AbstractUser):
    """Model for users"""

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    is_verified_email = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="user_images", null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    participation = models.IntegerField(default=0)
    create_event = models.IntegerField(default=0)
    wins = models.IntegerField(default=0)
    roles = models.ManyToManyField(to=Roles, blank=True, related_name="users_roles")
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = "пользователя"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"Пользователь {self.username} | {self.first_name}"


class EmailVerifications(models.Model):
    """Model for one emailverifications"""

    code = models.UUIDField(unique=True)
    text = models.CharField(max_length=512, null=True, blank=True)
    user = models.ForeignKey(to=Users, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()

    def __str__(self):
        return f"EmailVerification object for {self.user.email}"

    def send_verification_email(self):
        send_verification_email(self.user.email, self.code)

    def is_expired(self):
        is_expired(self)