from tempfile import NamedTemporaryFile
from urllib.request import urlopen

from django.core.files import File
from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers

from .models import Users


class ImageFieldFromURL(serializers.ImageField):
    def to_internal_value(self, data):
        # Проверяем, если data - это URL
        if data.startswith("http") or data.startswith("https"):
            # Открываем URL и читаем его содержимое
            response = urlopen(data)
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(response.read())
            img_temp.flush()
            # Создаем объект File из временного файла
            img = File(img_temp)
            # Возвращаем его как значение поля
            return img
        return super().to_internal_value(data)


class UserRegistSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = Users
        fields = ("id", "email", "username", "password")


class UserProfileSerializer(UserSerializer):
    photo = ImageFieldFromURL()

    class Meta(UserSerializer.Meta):
        model = Users
        fields = (
            "id",
            "username",
            "last_name",
            "wins",
            "description",
            "first_name",
            "photo",
            "email",
            "roles",
            "is_verified_email",
            "participation",
        )


class UserSerializer(UserSerializer):
    photo = ImageFieldFromURL()

    class Meta(UserSerializer.Meta):
        model = Users
        fields = ("id", "username", "last_name", "first_name", "photo")
        ref_name = "UserSerializerCustom"
