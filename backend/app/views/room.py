from rest_framework.response import Response
from rest_framework.views import APIView
from app import models
from app.serializers import RoomSerializer, RoomDetailSerializer
from app.permissions.room import RoomPermission
from app.utils.serializer_validator import validate_serializer


class Room(APIView):
    permission_classes = (RoomPermission,)

    # List rooms
    def get(self, request, hotel_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        return Response({
            'success': True,
            'rooms': RoomDetailSerializer(hotel.rooms, many=True).data
        })

    # Create room
    def post(self, request, hotel_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        self.check_object_permissions(request=request, obj=hotel)
        # Add type to context, room_type is missing after validate_serializer
        serializer = RoomSerializer(data=request.data, context={'hotel': hotel, 'type': request.data['room_type']})
        validate_serializer(serializer=serializer)
        # room = serializer.save()
        rooms = serializer.save()
        return Response({
            'success': True,
            # 'room': RoomDetailSerializer(room).data
            'rooms': RoomDetailSerializer(rooms, many=True).data
        })


class RoomDetail(APIView):
    permission_classes = (RoomPermission,)

    # Get one room
    def get(self, request, hotel_id, room_id):
        # hotel = models.Hotel.objects.get(uuid=hotel_id)
        room = models.Room.objects.get(uuid=room_id)
        return Response({
            'success': True,
            'room': RoomDetailSerializer(room).data
        })

    # Update room
    def put(self, request, hotel_id, room_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        room = models.Room.objects.get(uuid=room_id)
        [self.check_object_permissions(request=request, obj=obj) for obj in [hotel, room]]
        serializer = RoomSerializer(data=request.data, context={'hotel': hotel, 'type': request.data['room_type']})
        validate_serializer(serializer=serializer)
        serializer.update(instance=room, validated_data=serializer.validated_data)
        return Response({
            'success': True,
            'room': RoomDetailSerializer(room).data
        })

    # Delete room
    def delete(self, request, hotel_id, room_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        room = models.Room.objects.get(uuid=room_id)
        [self.check_object_permissions(request=request, obj=obj) for obj in [hotel, room]]
        room.delete()
        return Response({
            'success': True,
            'room': RoomDetailSerializer(room).data
        })
