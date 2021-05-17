from rest_framework import serializers
from app.models import Room, BookingRoom


class BookingRoomSerializer(serializers.Serializer):
    booking_id = serializers.CharField(required=False)
    room_numbers = serializers.ListField(required=False)

    def create(self, validated_data):
        validated_data['hotel_id'] = self.context['hotel'].uuid
        booking_id = validated_data['booking_id']
        booking_rooms = []
        for i in range(len(validated_data['room_numbers'])):
            room = Room.objects.filter(hotel_id=validated_data['hotel_id'], room_number=validated_data['room_numbers'][i])[0]
            booking_room = BookingRoom(booking_id=booking_id, room_id=room.uuid)
            booking_rooms.append(booking_room)
            booking_room.save()

        return booking_rooms

    def update(self, instance, validated_data):
        # Update booking
        [setattr(instance, field, value) for field, value in validated_data.items()]
        instance.save()
        return instance
