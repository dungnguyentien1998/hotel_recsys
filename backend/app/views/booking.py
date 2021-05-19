from rest_framework.response import Response
from rest_framework.views import APIView
from app import models
from app.serializers import BookingSerializer, BookingDetailSerializer
from app.permissions.booking import BookingPermission
from app.utils.serializer_validator import validate_serializer


# class Booking(APIView):
#     permission_classes = (BookingPermission,)
#
#     # List bookings, multiple
#     def get(self, request):
#         user = request.user
#         bookings = models.Booking.objects.filter(user_id=user.uuid)
#         createds = []
#         for booking in bookings:
#             createds.append(booking.created)
#         created_set = set(createds)
#         unique_created = list(created_set)
#         new_bookings = []
#         for created in unique_created:
#             temp_dict = {'created': '', 'check_in_time': '', 'check_out_time': '', 'user_id': '',
#                          'user_name': '', 'room_id': [], 'room_number': [], 'hotel_name': '', 'address': '',
#                          'room_type': [], 'price': [], 'image': '', 'hotelid': '', 'code': ''}
#             for booking in bookings:
#                 if booking.created == created:
#                     temp_dict['created'] = booking.created
#                     temp_dict['check_in_time'] = booking.check_in_time
#                     temp_dict['check_out_time'] = booking.check_out_time
#                     temp_dict['user_id'] = booking.user.uuid
#                     temp_dict['user_name'] = booking.user_name
#                     temp_dict['room_id'].append(booking.room.uuid)
#                     temp_dict['room_number'].append(booking.room_number)
#                     temp_dict['hotel_name'] = booking.hotel_name
#                     temp_dict['address'] = booking.address
#                     temp_dict['room_type'].append(booking.room_type)
#                     temp_dict['price'].append(booking.price)
#                     temp_dict['image'] = booking.image
#                     temp_dict['hotelid'] = booking.hotelid
#                     temp_dict['code'] = booking.code
#
#             new_bookings.append(temp_dict)
#         return Response({
#             'success': True,
#             # 'bookings': BookingDetailSerializer(new_bookings, many=True).data
#             'bookings': new_bookings
#         })
#
#     # Create booking
#     def post(self, request):
#         serializer = BookingSerializer(data=request.data, context={'request': request})
#         validate_serializer(serializer=serializer)
#         # booking = serializer.save()
#         bookings = serializer.save()
#         return Response({
#             'success': True,
#             # 'booking': BookingDetailSerializer(booking).data
#             'bookings': BookingDetailSerializer(bookings, many=True).data
#         })
#
#     def delete(self, request):
#         created = request.data['created']
#         user_id = request.user.uuid
#         bookings = models.Booking.objects.filter(created=created, user_id=user_id)
#         for booking in bookings:
#             booking.delete()
#         return Response({
#             'success': True,
#             'bookings': BookingDetailSerializer(bookings, many=True).data
#         })


# class BookingDetail(APIView):
#     permission_classes = (BookingPermission,)
#
#     # Get one booking
#     def get(self, request, booking_id):
#         booking = models.Booking.objects.get(uuid=booking_id)
#         return Response({
#             'success': True,
#             'booking': BookingDetailSerializer(booking).data
#         })
#
#     # Update booking
#     def put(self, request, booking_id):
#         booking = models.Booking.objects.get(uuid=booking_id)
#         self.check_object_permissions(request=request, obj=booking)
#         serializer = BookingSerializer(data=request.data, context={'request': request})
#         validate_serializer(serializer=serializer)
#         booking = serializer.update(instance=booking, validated_data=serializer.validated_data)
#         return Response({
#             'success': True,
#             'booking': BookingDetailSerializer(booking).data
#         })
#
#     # Delete booking
#     def delete(self, request, booking_id):
#         booking = models.Booking.objects.get(uuid=booking_id)
#         self.check_object_permissions(request=request, obj=booking)
#         booking.delete()
#         return Response({
#             'success': True,
#             'booking': BookingDetailSerializer(booking).data
#         })


# class HotelierBooking(APIView):
#     def get(self, request, hotel_id):
#         rooms = models.Room.objects.filter(hotel_id=hotel_id)
#         bookings = []
#         for room in rooms:
#             temp = models.Booking.objects.filter(room_id=room.uuid)
#             if len(temp) > 0:
#                 for temp_booking in temp:
#                     bookings.append(temp_booking)
#
#         user_ids = []
#         for booking in bookings:
#             user_ids.append(booking.user_id)
#         user_id_set = set(user_ids)
#         unique_user_id = list(user_id_set)
#         new_bookings = []
#         for user_id in unique_user_id:
#             user_bookings = []
#             for booking in bookings:
#                 if booking.user_id == user_id:
#                     user_bookings.append(booking)
#             createds = []
#             for booking in user_bookings:
#                 createds.append(booking.created)
#             created_set = set(createds)
#             unique_created = list(created_set)
#             for created in unique_created:
#                 temp_dict = {'created': '', 'check_in_time': '', 'check_out_time': '', 'user_id': '',
#                              'user_name': '', 'room_id': [], 'room_number': [], 'hotel_name': '', 'address': '',
#                              'room_type': [], 'price': [], 'image': '', 'hotelid': '', 'code': ''}
#                 for booking in user_bookings:
#                     if booking.created == created:
#                         temp_dict['created'] = booking.created
#                         temp_dict['check_in_time'] = booking.check_in_time
#                         temp_dict['check_out_time'] = booking.check_out_time
#                         temp_dict['user_id'] = booking.user.uuid
#                         temp_dict['user_name'] = booking.user_name
#                         temp_dict['room_id'].append(booking.room.uuid)
#                         temp_dict['room_number'].append(booking.room_number)
#                         temp_dict['hotel_name'] = booking.hotel_name
#                         temp_dict['address'] = booking.address
#                         temp_dict['room_type'].append(booking.room_type)
#                         temp_dict['price'].append(booking.price)
#                         temp_dict['image'] = booking.image
#                         temp_dict['hotelid'] = booking.hotelid
#                         temp_dict['code'] = booking.code
#                         temp_dict['user_email'] = booking.user_email
#                         temp_dict['user_tel'] = booking.user_tel
#
#                 new_bookings.append(temp_dict)
#
#         return Response({
#             'success': True,
#             'bookings': new_bookings
#         })
#
#     def delete(self, request, hotel_id):
#         created = request.data['created']
#         user_id = request.data['userId']
#         bookings = models.Booking.objects.filter(created=created, user_id=user_id)
#         for booking in bookings:
#             booking.delete()
#         return Response({
#             'success': True,
#             'bookings': BookingDetailSerializer(bookings, many=True).data
#         })

class Booking(APIView):
    def get(self, request):
        user = request.user
        bookings = models.Booking.objects.filter(user_id=user.uuid)
        return Response({
            'success': True,
            'bookings': BookingDetailSerializer(bookings, many=True).data
        })

    def post(self, request):
        serializer = BookingSerializer(data=request.data, context={'request': request})
        validate_serializer(serializer=serializer)
        booking = serializer.save()
        return Response({
            'success': True,
            'booking': BookingDetailSerializer(booking).data
        })


class BookingDetail(APIView):
    def get(self, request, booking_id):
        booking = models.Booking.objects.get(uuid=booking_id)
        return Response({
            'success': True,
            'booking': BookingDetailSerializer(booking).data
        })


class NewBooking(APIView):
    def get(self, request):
        user = request.user
        bookings = models.Booking.objects.filter(user_id=user.uuid)
        return Response({
            'success': True,
            'bookings': BookingDetailSerializer(bookings, many=True).data
        })

    def post(self, request):
        serializer = BookingSerializer(data=request.data, context={'request': request})
        validate_serializer(serializer=serializer)
        booking = serializer.save()
        return Response({
            'success': True,
            'booking': BookingDetailSerializer(booking).data
        })


class NewBookingDetail(APIView):
    def get(self, request, booking_id):
        booking = models.Booking.objects.get(uuid=booking_id)
        return Response({
            'success': True,
            'booking': BookingDetailSerializer(booking).data
        })

    def delete(self, request, booking_id):
        booking = models.Booking.objects.get(uuid=booking_id)
        booking.delete()
        response_data = BookingDetailSerializer(booking).data
        booking_rooms = models.BookingRoom.objects.filter(booking_id=booking_id)
        for booking_room in booking_rooms:
            booking_room.delete()
        return Response({
            'success': True,
            'booking': response_data
        })


class NewHotelierBooking(APIView):
    def get(self, request, hotel_id):
        # rooms = models.Room.objects.filter(hotel_id=hotel_id)
        # types = models.Type.objects.filter(hotel_id=hotel_id)
        # booking_ids = []
        # for room_type in types:
        #     temp = models.BookingType.objects.filter(type_id=room_type.uuid)
        #     if len(temp) > 0:
        #         for temp_booking_type in temp:
        #             booking_ids.append(temp_booking_type.booking_id)
        #
        # unique_booking_ids = list(set(booking_ids))
        # bookings = []
        # for uuid in unique_booking_ids:
        #     booking = models.Booking.objects.get(uuid=uuid)
        #     bookings.append(booking)

        bookings = models.Booking.objects.filter(hotel_id=hotel_id)

        return Response({
            'success': True,
            'bookings': BookingDetailSerializer(bookings, many=True).data
        })


class NewHotelierBookingDetail(APIView):
    # Get the available rooms from all room type in an user booking
    def get(self, request, hotel_id, booking_id):
        booking = models.Booking.objects.get(uuid=booking_id)
        check_in_time = booking.check_in_time
        check_out_time = booking.check_out_time

        booking_types = models.BookingType.objects.filter(booking_id=booking_id)
        booking_rooms = models.BookingRoom.objects.filter(booking_id=booking_id)
        room_types = []
        for booking_type in booking_types:
            temp_dict = {'room_type': '', 'room_number': [], 'amount': 0, 'room_booked': []}
            room_type = models.Type.objects.get(uuid=booking_type.type_id)
            temp_dict['room_type'] = room_type.room_type
            temp_dict['amount'] = booking_type.count
            rooms = models.Room.objects.filter(type_id=room_type.uuid)
            for room in rooms:
                current_booking_rooms = models.BookingRoom.objects.filter(room_id=room.uuid)
                check = True
                for current_booking_room in current_booking_rooms:
                    current_booking = models.Booking.objects.get(uuid=current_booking_room.booking_id)
                    if current_booking.check_in_time < check_out_time <= current_booking.check_out_time:
                        check = False
                        break
                    if check_out_time > current_booking.check_out_time > check_in_time:
                        check = False
                        break

                if check:
                    temp_dict['room_number'].append(room.room_number)

            for booking_room in booking_rooms:
                room = models.Room.objects.get(uuid=booking_room.room_id)
                if room.room_type == room_type.room_type:
                    temp_dict['room_booked'].append(room.room_number)

            room_types.append(temp_dict)

        return Response({
            'success': True,
            'types': room_types
        })

    def delete(self, request, hotel_id, booking_id):
        booking = models.Booking.objects.get(uuid=booking_id)
        booking.delete()
        response_data = BookingDetailSerializer(booking).data
        booking_rooms = models.BookingRoom.objects.filter(booking_id=booking_id)
        for booking_room in booking_rooms:
            booking_room.delete()
        return Response({
            'success': True,
            'booking': response_data
        })