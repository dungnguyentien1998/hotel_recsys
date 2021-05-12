import json

from app.models import Booking, Room, Type
from app.exceptions import ValidationError, BookingError
from rest_framework import serializers
from datetime import datetime


# Booking crud
class BookingSerializer(serializers.Serializer):
    # Booking data
    check_in_time = serializers.DateTimeField(required=False)
    check_out_time = serializers.DateTimeField(required=False)
    # room_id = serializers.CharField(required=False)

    # hotel_id = serializers.CharField(required=False)
    # room_type = serializers.CharField(required=False)
    # booking_count = serializers.IntegerField(required=False)

    hotel_id = serializers.CharField(required=False)
    room_types = serializers.ListField(required=False)
    booking_counts = serializers.ListField(required=False, child=serializers.IntegerField())

    # Create one booking, without booking_count
    # def create(self, validated_data):
    #     # Get user id and room
    #     validated_data['user_id'] = self.context['request'].user.uuid
    #     rooms = Room.objects.filter(room_type=validated_data['room_type'], hotel_id=validated_data['hotel_id'])
    #     # room = Room.objects.get(uuid=validated_data['room_id'])
    #     check = True
    #     for room in rooms:
    #         current_bookings = Booking.objects.filter(room_id=room.uuid)
    #         # Check is used to validate new booking
    #         check = True
    #         for current_booking in current_bookings:
    #             if current_booking.check_in_time < validated_data['check_out_time'] <= current_booking.check_out_time:
    #                 check = False
    #                 break
    #             if validated_data['check_out_time'] > current_booking.check_out_time > validated_data['check_in_time']:
    #                 check = False
    #                 break
    #
    #         if check:
    #             validated_data.pop('room_type')
    #             validated_data.pop('hotel_id')
    #             validated_data['room_id'] = room.uuid
    #             booking = Booking.objects.create(**validated_data)
    #             # Update room booked count attribute and create booking
    #             room.booked_count += 1
    #             room.save()
    #             return booking
    #
    #     if not check:
    #         raise ValidationError('Room booked')

    # Create multiple booking, with one room type
    # def create(self, validated_data):
    #     # Get user id and room
    #     validated_data['user_id'] = self.context['request'].user.uuid
    #     rooms = Room.objects.filter(room_type=validated_data['room_type'], hotel_id=validated_data['hotel_id'])
    #     count = 0
    #     room_ids = []
    #     for room in rooms:
    #         current_bookings = Booking.objects.filter(room_id=room.uuid)
    #         # Check is used to validate new booking
    #         check = True
    #         for current_booking in current_bookings:
    #             if current_booking.check_in_time < validated_data['check_out_time'] <= current_booking.check_out_time:
    #                 check = False
    #                 break
    #             if validated_data['check_out_time'] > current_booking.check_out_time > validated_data['check_in_time']:
    #                 check = False
    #                 break
    #
    #         if check:
    #             count += 1
    #             room_ids.append(room.uuid)
    #
    #         if count == validated_data['booking_count']:
    #             break
    #
    #     if count < validated_data['booking_count']:
    #         raise ValidationError('Room booked')
    #
    #     validated_data.pop('room_type')
    #     validated_data.pop('hotel_id')
    #     validated_data.pop('booking_count')
    #     bookings = []
    #     for room_id in room_ids:
    #         validated_data['room_id'] = room_id
    #         booking = Booking.objects.create(**validated_data)
    #         bookings.append(booking)
    #     return bookings

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
        bookings = []
        room_ids = []
        remains = {}
        get_avaiable = True
        for i in range(len(booking_counts)):
            if booking_counts[i] > 0:
                get_avaiable = False

        final = True
        for i in range(len(room_types)):
            room_type = Type.objects.filter(room_type=room_types[i], hotel_id=hotel_id)[0]
            rooms = Room.objects.filter(type_id=room_type.uuid)
            count = 0
            for room in rooms:
                current_bookings = Booking.objects.filter(room_id=room.uuid)
                # Check is used to validate new booking
                check = True
                for current_booking in current_bookings:
                    if current_booking.check_in_time < validated_data['check_out_time'] <= current_booking.check_out_time:
                        check = False
                        break
                    if validated_data['check_out_time'] > current_booking.check_out_time > validated_data['check_in_time']:
                        check = False
                        break

                if check:
                    if count < booking_counts[i]:
                        room_ids.append(room.uuid)
                    count += 1

                # if count == booking_counts[i]:
                #     break

            remains[room_types[i]] = count
            if count < booking_counts[i]:
                final = False
                # remains[room_types[i]] = count
                # raise ValidationError('Room booked')

        failed_message = ''
        for key in remains.keys():
            failed_message += str(remains[key]) + " " + key + ", "

        if (not final) or get_avaiable:
            raise BookingError(json.dumps(remains))

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
        now_string = now.strftime("%Y-%m-%d %H:%M:%S")
        for room_id in room_ids:
            validated_data['room_id'] = room_id
            # booking = Booking.objects.create(**validated_data)
            booking = Booking(check_in_time=validated_data['check_in_time'], check_out_time=validated_data['check_out_time'],
                              user_id=validated_data['user_id'], room_id=validated_data['room_id'],
                              created=now, updated=now, code=code)
            bookings.append(booking)
            booking.save()

        return bookings

    def update(self, instance, validated_data):
        # Update booking
        [setattr(instance, field, value) for field, value in validated_data.items()]
        instance.save()
        return instance


class BookingDetailSerializer(serializers.ModelSerializer):
    # Booking data used to represent
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
