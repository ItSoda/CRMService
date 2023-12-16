from rest_framework import serializers

from users.models import Users
from users.serializers import ImageFieldFromURL, UserSerializer

from .models import Events, Reviews, Tags, Teams


class TagSerializer(serializers.Serializer):
    class Meta:
        model = Tags
        fields = "__all__"


class TeamCreateSerializer(serializers.Serializer):
    members = serializers.ListField(child=serializers.IntegerField(), write_only=True)

    class Meta:
        model = Teams
        fields = "__all__"

    def create(self, validated_data):
        members_ids = validated_data.pop("members")
        instance = Teams.objects.create(**validated_data)
        instance.members.set(members_ids)

        return instance

    def update(self, instance, validated_data):
        members_ids = validated_data.pop("members")
        if not [
            member for member in members_ids if member in instance.events_participian
        ]:
            instance.members.add(members_ids)
            return instance


class TeamSerializer(serializers.Serializer):
    members = UserSerializer(many=True)

    class Meta:
        model = Teams
        fields = "__all__"


class EventCreateSerializer(serializers.ModelSerializer):
    teams = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    participian = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )
    winners = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    tags = serializers.ListField(child=serializers.IntegerField(), write_only=True)
    creator = serializers.IntegerField(write_only=True)

    class Meta:
        model = Events
        fields = "__all__"

    def create(self, validated_data):
        participian_ids = validated_data.pop("participian")
        teams_ids = validated_data.pop("teams")
        winners_ids = validated_data.pop("winners")
        tags_ids = validated_data.pop("tags")
        creator_id = validated_data.pop("creator")
        creator = Users.objects.get(id=creator_id)

        instance = Events.objects.create(creator=creator, **validated_data)
        instance.teams.set(teams_ids)
        instance.participian.set(participian_ids)
        instance.winners.set(winners_ids)
        instance.tags.set(tags_ids)
        return instance


class EventSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)
    teams = TeamSerializer(many=True)
    participian = UserSerializer(many=True)
    winners = UserSerializer(many=True)
    creator = UserSerializer()
    image = ImageFieldFromURL()

    class Meta:
        model = Events
        fields = "__all__"


class ReviewCreateSerializer(serializers.ModelSerializer):
    event = serializers.IntegerField(write_only=True)
    user = serializers.IntegerField(write_only=True)

    class Meta:
        model = Reviews
        fields = "__all__"

    def create(self, validated_data):
        event_id = validated_data.pop("event")
        user_id = validated_data.pop("user")

        user = Users.objects.get(id=user_id)
        event = Events.objects.get(id=event_id)

        instance = Events.objects.create(user=user, event=event, **validated_data)
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    event = EventSerializer()
    user = UserSerializer()

    class Meta:
        model = Reviews
        fields = "__all__"
