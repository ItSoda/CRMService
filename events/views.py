from rest_framework.viewsets import ModelViewSet
from events.permissions import IsCreatorUser
from events.services import event_update_participation, event_update_winner, user_update_participation, user_update_winner
from .models import Events, Reviews, Teams
from .serializers import EventSerializer, EventCreateSerializer, ReviewSerializer, ReviewCreateSerializer, TeamCreateSerializer, TeamSerializer
from rest_framework.permissions import AllowAny
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response


class EventViewSet(ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    permission_classes = (AllowAny,)

    @method_decorator(cache_page(70))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.get_serializer = EventCreateSerializer
        return super().create(request, *args, **kwargs)
    

@api_view(["POST"])
def add_participants(request, event_id):
    try:
        data = request.data
        user_id = data.get("user_id")
        user_update_participation(user_id, event_id)
        event = event_update_participation(user_id, event_id)

        serializer_data = EventSerializer(event).data
        return Response({"status_code": 200, "data": serializer_data, "detail": "Participant add in events"})
    except Exception as e:
        return Response({"status_code": 500, "data": [], "detail": f"Error: {str(e)}"})


@api_view(["POST"])
def add_winners(request, event_id):
    try:
        data = request.data
        user_id = data.get("user_id")
        user_update_winner(user_id, event_id)
        event = event_update_winner(user_id, event_id)

        serializer_data = EventSerializer(event).data
        return Response({"status_code": 200, "data": serializer_data, "detail": "Winner add in events"})
    except Exception as e:
        return Response({"status_code": 500, "data": [], "detail": f"Error: {str(e)}"})


class TeamViewSet(ModelViewSet):
    queryset = Teams.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (AllowAny,)

    @method_decorator(cache_page(70))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.get_serializer = TeamCreateSerializer
        return super().create(request, *args, **kwargs)
    

class ReviewViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (AllowAny,)

    def get_permissions(self):
        if self.action in ["create", "destroy", "update", "partial_update"]:
            permission_classes = [IsCreatorUser]
        elif self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        event_id = self.request.GET.get("event_id")
        return queryset.filter(event=event_id)
    
    @method_decorator(cache_page(100))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        self.get_serializer = ReviewCreateSerializer
        return super().create(request, *args, **kwargs)
