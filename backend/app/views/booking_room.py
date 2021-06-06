from rest_framework.response import Response
from rest_framework.views import APIView
from app import models
from app.serializers import BookingRoomSerializer, BookingRoomDetailSerializer, BookingDetailSerializer
from app.utils.serializer_validator import validate_serializer


class BookingRoomDetail(APIView):
    def get(self, request, hotel_id):
        booking_rooms = models.BookingRoom.objects.filter(booking_id=request.query_params['bookingId'])
        return Response({
            'success': True,
            'booking_rooms': BookingRoomDetailSerializer(booking_rooms, many=True).data
        })

    # Assign rooms
    def post(self, request, hotel_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        serializer = BookingRoomSerializer(data=request.data, context={'hotel': hotel})
        validate_serializer(serializer=serializer)
        booking_rooms = serializer.save()
        return Response({
            'success': True,
        })


class BookingRoom(APIView):
    def get(self, request, hotel_id):
        bookings = models.Booking.objects.filter(hotel_id=hotel_id)
        new_bookings = []
        for booking in bookings:
            booking_rooms = models.BookingRoom.objects.filter(booking_id=booking.uuid)
            if len(booking_rooms) <= 0:
                new_bookings.append(booking)

        return Response({
            'success': True,
            'bookings': BookingDetailSerializer(new_bookings, many=True).data
        })
