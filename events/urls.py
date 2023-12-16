from django.urls import include, path
from rest_framework import routers

from .views import EventViewSet, ReviewViewSet, add_participants, add_winners

app_name = "animals"

router = routers.DefaultRouter()
router.register(r"events", EventViewSet, basename="events")
router.register(r"reviews", ReviewViewSet, basename="reviews")

urlpatterns = [
    path("", include(router.urls)),
    path("add/participant/<int:event_id>/", add_participants, name="add-participants"),
    path("add/winner/<int:event_id>/", add_winners, name="add-winners"),
]