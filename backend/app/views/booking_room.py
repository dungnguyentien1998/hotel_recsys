from rest_framework.response import Response
from rest_framework.views import APIView
from app import models
from app.serializers import BookingRoomSerializer
from app.utils.serializer_validator import validate_serializer


class BookingRoom(APIView):
    def post(self, request, hotel_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        serializer = BookingRoomSerializer(data=request.data, context={'hotel': hotel})
        validate_serializer(serializer=serializer)
        booking_rooms = serializer.save()
        return Response({
            'success': True,
        })
