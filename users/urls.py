from django.urls import include, path
from rest_framework import routers

from .views import (EmailVerificationAndUserUpdateView, UserSearchView,
                    UserViewSets)

app_name = "users"

router = routers.DefaultRouter()
router.register("users", UserViewSets, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    path("users/search/", UserSearchView.as_view(), name="search"),
    path(
        "verify/<str:email>/<uuid:code>/",
        EmailVerificationAndUserUpdateView.as_view(),
        name="email_verify",
    ),
]
