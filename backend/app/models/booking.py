import datetime
from django.db import models
from app.models.user import User
from app.models.room import Room
from app.utils.model_maker import BaseModel
from django.conf import settings


# Booking model
class Booking(BaseModel):
    check_in_time = models.DateTimeField(null=True)
    check_out_time = models.DateTimeField(null=True)
    # user = models.ForeignKey(User, related_name='bookings', on_delete=models.SET_NULL, null=True)
    # room = models.ForeignKey(Room, related_name='bookings', on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, related_name='bookings', on_delete=models.DO_NOTHING, null=True)
    room = models.ForeignKey(Room, related_name='bookings', on_delete=models.DO_NOTHING, null=True)
    code = models.CharField(null=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    created = models.DateTimeField(blank=True)
    updated = models.DateTimeField(blank=True)

    @property
    def user_name(self):
        return self.user.name

    @property
    def hotel_name(self):
        return self.room.hotel.name

    @property
    def room_number(self):
        return self.room.room_number

    @property
    def address(self):
        if (not self.room.hotel.address) or self.room.hotel.address == "":
            return self.room.hotel.ward + ', ' + self.room.hotel.district + ', ' + self.room.hotel.city
        else:
            return self.room.hotel.address + ', ' + self.room.hotel.ward + ', ' + \
                   self.room.hotel.district + ', ' + self.room.hotel.city

    @property
    def room_type(self):
        return self.room.room_type

    @property
    def price(self):
        first_date = datetime.datetime.date(self.check_in_time)
        last_date = datetime.datetime.date(self.check_out_time)
        delta = last_date - first_date
        return self.room.price * delta.days

    @property
    def image(self):
        return self.room.hotel.image.url

    @property
    def hotelid(self):
        return self.room.hotel.uuid

    @property
    def user_email(self):
        return self.user.email

    @property
    def user_tel(self):
        return self.user.tel

    class Meta:
        db_table = 'booking'
