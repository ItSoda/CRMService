from django.urls import include, path
from rest_framework import routers

from .views import (EventViewSet, ReviewViewSet, TeamViewSet, add_participants,
                    add_winners, get_team)

app_name = "animals"

router = routers.DefaultRouter()
router.register(r"events", EventViewSet, basename="events")
router.register(r"reviews", ReviewViewSet, basename="reviews")
router.register(r"teams", TeamViewSet, basename="teams")

urlpatterns = [
    path("", include(router.urls)),
    path("get_team/<int:user_id>/", get_team, name="get-team"),
    path("add/participant/<int:event_id>/", add_participants, name="add-participants"),
    path("add/winner/<int:event_id>/", add_winners, name="add-winners"),
]
