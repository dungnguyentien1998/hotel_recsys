import datetime
import random

from django.db import models
from app.models.user import User
from app.models.room import Room
from app.models.type import Type
from app.models.hotel import Hotel
from app.utils.model_maker import BaseModel
from django.conf import settings


# Booking model
class Booking(BaseModel):
    check_in_time = models.DateTimeField(null=True)
    check_out_time = models.DateTimeField(null=True)
    # user = models.ForeignKey(User, related_name='bookings', on_delete=models.SET_NULL, null=True)
    # room = models.ForeignKey(Room, related_name='bookings', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.SET_NULL, null=True)
    rooms = models.ManyToManyField(Room, through='BookingRoom')
    types = models.ManyToManyField(Type, through='BookingType')
    code = models.CharField(null=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(blank=True)
    total_price = models.PositiveBigIntegerField(null=True)
    hotel_id = models.CharField(null=True, max_length=settings.CHAR_FIELD_MAX_LEN)

    @property
    def user_name(self):
        return self.user.name

    @property
    def hotel_name(self):
        from app.models.booking_type import BookingType
        booking_type = BookingType.objects.filter(booking_id=self.uuid)[0]
        room_type = Type.objects.get(uuid=booking_type.type_id)
        return room_type.hotel.name

    @property
    def room_number(self):
        from app.models.booking_room import BookingRoom
        room_number = []
        booking_rooms = BookingRoom.objects.filter(booking_id=self.uuid)
        for booking_room in booking_rooms:
            room = Room.objects.get(uuid=booking_room.room_id)
            room_number.append(room.room_number)
        return room_number

    @property
    def address(self):
        from app.models.booking_type import BookingType
        booking_type = BookingType.objects.filter(booking_id=self.uuid)[0]
        room_type = Type.objects.get(uuid=booking_type.type_id)

        if (not room_type.hotel.address) or room_type.hotel.address == "":
            return ''
        else:
            return room_type.hotel.address

    @property
    def city(self):
        from app.models.booking_type import BookingType
        booking_type = BookingType.objects.filter(booking_id=self.uuid)[0]
        room_type = Type.objects.get(uuid=booking_type.type_id)
        return room_type.hotel.city

    @property
    def district(self):
        from app.models.booking_type import BookingType
        booking_type = BookingType.objects.filter(booking_id=self.uuid)[0]
        room_type = Type.objects.get(uuid=booking_type.type_id)
        return room_type.hotel.district

    @property
    def ward(self):
        from app.models.booking_type import BookingType
        booking_type = BookingType.objects.filter(booking_id=self.uuid)[0]
        room_type = Type.objects.get(uuid=booking_type.type_id)
        return room_type.hotel.ward

    @property
    def room_type(self):
        from app.models.booking_type import BookingType
        room_type = []
        booking_types = BookingType.objects.filter(booking_id=self.uuid)
        for booking_type in booking_types:
            temp_room_type = Type.objects.get(uuid=booking_type.type_id)
            room_type.append(temp_room_type.name)
        return room_type

    def room_amount(self):
        from app.models.booking_type import BookingType
        room_amount = []
        booking_types = BookingType.objects.filter(booking_id=self.uuid)
        for booking_type in booking_types:
            room_amount.append(booking_type.count)
        return room_amount

    @property
    def price(self):
        from app.models.booking_type import BookingType
        price = []
        first_date = datetime.datetime.date(self.check_in_time)
        last_date = datetime.datetime.date(self.check_out_time)
        delta = last_date - first_date
        booking_types = BookingType.objects.filter(booking_id=self.uuid)
        for booking_type in booking_types:
            room_type = Type.objects.get(uuid=booking_type.type_id)
            price.append(room_type.price * delta.days * booking_type.count)
        return price

    @property
    def image(self):
        from app.models.booking_type import BookingType
        booking_type = BookingType.objects.filter(booking_id=self.uuid)[0]
        room_type = Type.objects.get(uuid=booking_type.type_id)
        return room_type.hotel.image.url

    @property
    def hotelid(self):
        from app.models.booking_type import BookingType
        booking_type = BookingType.objects.filter(booking_id=self.uuid)[0]
        room_type = Type.objects.get(uuid=booking_type.type_id)
        return room_type.hotel.uuid

    @property
    def user_email(self):
        return self.user.email

    @property
    def user_tel(self):
        return self.user.tel

    @property
    def hotel_owner_id(self):
        hotel = Hotel.objects.get(uuid=self.hotel_id)
        return hotel.user.uuid

    class Meta:
        db_table = 'booking'
