from rest_framework import serializers
from .room import RoomSerializer, RoomDetailSerializer
from app.models import BookingRoom


class BookingRoomSerializer(serializers.ModelSerializer):
    room = RoomSerializer()

    class Meta:
        model = BookingRoom
        fields = BookingRoom.get_fields()
