import json

from asgiref.sync import async_to_sync, sync_to_async
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models import Q
from djangochannelsrestframework import mixins
from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.observer import model_observer
from djangochannelsrestframework.observer.generics import (
    ObserverModelInstanceMixin, action)

from users.models import Users

from .models import Message, Room
from .serializers import MessageSerializer, RoomSerializer, UserSerializer


class RoomConsumer(ObserverModelInstanceMixin, GenericAsyncAPIConsumer):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = "pk"

    async def connect(self):
        await self.accept()

    async def disconnect(self, code):
        await super().disconnect(code)

    # @action()
    # async def join_room(self, pk, **kwargs):
    #     self.room_subscribe = pk
    #     await self.add_user_to_room(pk)
    #     await self.notify_users()

    # @action()
    # async def leave_room(self, pk, **kwargs):
    #     await self.remove_user_from_room(pk)

    @action()
    async def create_message(self, message, image=None, **kwargs):
        room: Room = await self.get_room(1)
        await database_sync_to_async(Message.objects.create)(
            sender=self.scope["user"], text=message, image=image, room=room
        )

    # Подписка на все методы message_activity
    @action()
    async def subscribe_to_messages_in_room(self, **kwargs):
        room: Room = await self.get_room(1)
        await self.message_activity.subscribe(room=room)

    # Следит за обновлениями сообщений
    @model_observer(Message)
    async def message_activity(self, message, observer=None, **kwargs):
        await self.send_json(message)

    # @message_activity.groups_for_signal
    # def message_activity(self, instance: Message, **kwargs):
    #     yield f"room__{instance.room_id}"
    #     yield f"pk__{instance.pk}"

    # @message_activity.groups_for_consumer
    # def message_activity(self, room=None, **kwargs):
    #     if room is not None:
    #         yield f"room__{room}"

    @message_activity.serializer
    def message_activity(self, instance: Message, action, **kwargs):
        room_id = 1
        return dict(
            data=MessageSerializer(instance).data, action=action.value, pk=room_id
        )

    @database_sync_to_async
    def get_room(self, room_pk):
        return Room.objects.get(pk=room_pk)

    # async def notify_users(self):
    #     room: Room = await self.get_room(self.room_subscribe)
    #     for group in self.groups:
    #         await self.channel_layer.group_send(
    #             group,
    #             {"type": "update_users", "usuarios": await self.current_users(room)},
    #         )

    # async def update_users(self, event: dict):
    #     await self.send(text_data=json.dumps({"usuarios": event["usuarios"]}))

    # @database_sync_to_async
    # def get_room(self, pk: int) -> Room:
    #     return Room.objects.get(pk=pk)

    # @database_sync_to_async
    # def current_users(self, room: Room):
    #     return [UserSerializer(user).data for user in room.current_users.all()]

    # @database_sync_to_async
    # def remove_user_from_room(self, room):
    #     user: Users = self.scope["user"]
    #     user.current_rooms.remove(room)

    # @database_sync_to_async
    # def add_user_to_room(self, pk):
    #     user: Users = self.scope["user"]
    #     if not user.current_rooms.filter(pk=self.room_subscribe).exists():
    #         user.current_rooms.add(Room.objects.get(pk=pk))


class UserConsumer(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.PatchModelMixin,
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.DeleteModelMixin,
    GenericAsyncAPIConsumer,
):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

from .models import PersonalMessage


# need work
class UserChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_pk = self.scope["url_route"]["kwargs"]["user_pk"]
        self.room_group_name = f"personalchat_{self.user_pk}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data["message"]
        sender = self.scope["user"]
        receiver = await self.get_receiver(self.user_pk)
        # # Save message to database
        await self.save_message(sender, receiver, message)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))

    @staticmethod
    @sync_to_async
    def save_message(sender, receiver, message, image=None):
        PersonalMessage.objects.create(
            sender=sender, receiver=receiver, text=message, image=image
        )

    @staticmethod
    @sync_to_async
    def get_receiver(user_pk):
        return Users.objects.get(id=user_pk)
