import json

from app.models import Booking, Room, Type, BookingRoom, BookingType, Hotel
from app.exceptions import ValidationError, BookingError
from rest_framework import serializers
from datetime import datetime


# Booking crud
class BookingSerializer(serializers.Serializer):
    # Booking data
    check_in_time = serializers.DateTimeField(required=False)
    check_out_time = serializers.DateTimeField(required=False)

    hotel_id = serializers.CharField(required=False)
    room_types = serializers.ListField(required=False)
    booking_counts = serializers.ListField(required=False, child=serializers.IntegerField())

    # Create multiple booking, with multiple room type
    def create(self, validated_data):
        # Get user id and room
        validated_data['user_id'] = self.context['request'].user.uuid
        if len(validated_data['room_types']) != len(validated_data['booking_counts']):
            raise ValidationError('Room types and booking counts must be equal')

        room_types = validated_data['room_types']
        booking_counts = validated_data['booking_counts']
        hotel_id = validated_data['hotel_id']
        validated_data.pop('room_types')
        validated_data.pop('hotel_id')
        validated_data.pop('booking_counts')
        remains = {}
        get_avaiable = True
        for i in range(len(booking_counts)):
            if booking_counts[i] > 0:
                get_avaiable = False

        final = True
        # Get number of rooms available for each room type
        for i in range(len(room_types)):
            room_type = Type.objects.filter(room_type=room_types[i], hotel_id=hotel_id)[0]
            rooms = Room.objects.filter(type_id=room_type.uuid)
            count = 0
            current_booking_types = BookingType.objects.filter(type_id=room_type.uuid)
            for current_booking_type in current_booking_types:
                current_booking = Booking.objects.get(uuid=current_booking_type.booking_id)
                if current_booking.check_in_time < validated_data['check_out_time'] <= current_booking.check_out_time:
                    count += current_booking_type.count
                elif validated_data['check_out_time'] > current_booking.check_out_time > validated_data['check_in_time']:
                    count += current_booking_type.count

            remains[room_types[i]] = len(rooms) - count
            if remains[room_types[i]] < booking_counts[i]:
                final = False

            # for room in rooms:
            #     current_booking_rooms = BookingRoom.objects.filter(room_id=room.uuid)
            #     # Check is used to validate new booking
            #     check = True
            #     for current_booking_room in current_booking_rooms:
            #         current_booking = Booking.objects.get(uuid=current_booking_room.booking_id)
            #         if current_booking.check_in_time < validated_data['check_out_time'] <= current_booking.check_out_time:
            #             check = False
            #             break
            #         if validated_data['check_out_time'] > current_booking.check_out_time > validated_data['check_in_time']:
            #             check = False
            #             break
            #
            #     if check:
            #         count += 1
            #
            # remains[room_types[i]] = count
            # if count < booking_counts[i]:
            #     final = False

        if (not final) or get_avaiable:
            raise BookingError(json.dumps(remains))

        # If there are enough rooms to book
        now = datetime.now()
        year = str(now.year)
        month = str(now.month)
        day = str(now.day)
        year = year[2:len(year)]
        if len(month) == 1:
            month = "0" + month
        if len(day) == 1:
            day = "0" + day
        hour = str(now.hour)
        minute = str(now.minute)
        second = str(now.second)
        microsecond = str(now.microsecond)
        if len(hour) == 1:
            hour = "0" + hour
        if len(minute) == 1:
            minute = "0" + minute
        if len(second) == 1:
            second = "0" + second
        microsecond = microsecond[0:4]
        code = year + month + day + hour + minute + second + microsecond

        total_price = 0
        first_date = datetime.date(validated_data['check_in_time'])
        last_date = datetime.date(validated_data['check_out_time'])
        delta = last_date - first_date
        for i in range(len(room_types)):
            room_type = Type.objects.filter(room_type=room_types[i], hotel_id=hotel_id)[0]
            total_price = total_price + room_type.price * booking_counts[i] * delta.days

        booking = Booking(check_in_time=validated_data['check_in_time'], check_out_time=validated_data['check_out_time'],
                          user_id=validated_data['user_id'], created=now, updated=now, code=code,
                          total_price=total_price, hotel_id=hotel_id)
        booking.save()
        booking_id = booking.uuid

        for i in range(len(room_types)):
            if booking_counts[i] > 0:
                room_type = Type.objects.filter(room_type=room_types[i], hotel_id=hotel_id)[0]
                booking_type = BookingType(booking_id=booking_id, type_id=room_type.uuid, count=booking_counts[i])
                booking_type.save()

        return booking

    def update(self, instance, validated_data):
        # Update booking
        [setattr(instance, field, value) for field, value in validated_data.items()]
        instance.save()
        return instance


class BookingDetailSerializer(serializers.ModelSerializer):
    user_name = serializers.ReadOnlyField()
    hotel_name = serializers.ReadOnlyField()
    room_number = serializers.ReadOnlyField()
    address = serializers.ReadOnlyField()
    room_type = serializers.ReadOnlyField()
    price = serializers.ReadOnlyField()
    image = serializers.ReadOnlyField()
    hotelid = serializers.ReadOnlyField()
    user_email = serializers.ReadOnlyField()
    user_tel = serializers.ReadOnlyField()

    class Meta:
        model = Booking
        fields = [*Booking.get_fields(), 'user_name', 'hotel_name', 'room_number', 'address', 'room_type', 'price',
                  'image', 'hotelid', 'user_email', 'user_tel']
