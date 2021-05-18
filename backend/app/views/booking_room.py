from rest_framework.response import Response
from rest_framework.views import APIView
from app import models
from app.serializers import BookingRoomSerializer, BookingRoomDetailSerializer
from app.utils.serializer_validator import validate_serializer


class BookingRoom(APIView):
    def get(self, request, hotel_id):
        # booking = models.Booking.objects.get(uuid=request.data['booking_id'])
        booking_rooms = models.BookingRoom.objects.filter(booking_id=request.query_params['bookingId'])
        return Response({
            'success': True,
            'booking_rooms': BookingRoomDetailSerializer(booking_rooms, many=True).data
        })

    def post(self, request, hotel_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        serializer = BookingRoomSerializer(data=request.data, context={'hotel': hotel})
        validate_serializer(serializer=serializer)
        booking_rooms = serializer.save()
        return Response({
            'success': True,
        })
