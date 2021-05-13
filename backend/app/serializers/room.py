from app.models import Room, Type
from rest_framework import serializers
from app.exceptions import ValidationError


# Room crud
class RoomSerializer(serializers.ModelSerializer):
    room_numbers = serializers.ListField(required=False)
    images = serializers.ListField(required=False)

    # Room data
    class Meta:
        model = Room
        fields = [*Room.editable_fields(), 'room_numbers', 'images']

    # Create multiple room, with same room type
    # Data: room_numbers and images
    def create(self, validated_data):
        validated_data['hotel_id'] = self.context['hotel'].uuid
        # Add type to context, room_type is missing after validate_serializer
        validated_data['room_type'] = self.context['type']
        room_type = Type.objects.filter(room_type=validated_data['room_type'], hotel_id=validated_data['hotel_id'])[0]

        if len(validated_data['room_numbers']) != len(validated_data['images']):
            raise ValidationError('Room numbers and images must be equal')

        # Create room
        rooms = []
        for i in range(len(validated_data['room_numbers'])):
            current_rooms = Room.objects.filter(hotel_id=validated_data['hotel_id'], room_number=validated_data['room_numbers'][i])
            if len(current_rooms) > 0:
                raise ValidationError(validated_data['room_numbers'][i])
            room = Room(room_number=validated_data['room_numbers'][i], image=validated_data['images'][i],
                        hotel_id=validated_data['hotel_id'], type_id=room_type.uuid)
            rooms.append(room)
            room.save()
        return rooms

    def update(self, instance, validated_data):
        # Update room
        # Add type to context, room_type is missing after validate_serializer
        if validated_data['room_number'] != 'null':
            current_rooms = Room.objects.filter(hotel_id=self.context['hotel'].uuid, room_number=validated_data['room_number'])
            if len(current_rooms) > 0:
                raise ValidationError('Room number ' + validated_data['room_number'] + ' already exist')
        else:
            validated_data.pop('room_number')
        [setattr(instance, field, value) for field, value in validated_data.items()]
        room_type = Type.objects.filter(room_type=self.context['type'])[0]
        instance.type_id = room_type.uuid
        instance.save()
        return instance


class RoomDetailSerializer(serializers.ModelSerializer):
    # Room data used to represent
    # from app.serializers.booking import BookingDetailSerializer
    # bookings = BookingDetailSerializer(many=True)
    room_type = serializers.ReadOnlyField()
    capacity = serializers.ReadOnlyField()
    price = serializers.ReadOnlyField()
    amenities = serializers.ReadOnlyField()

    class Meta:
        model = Room
        fields = [*Room.get_fields(), 'bookings', 'room_type', 'capacity', 'price', 'amenities']
