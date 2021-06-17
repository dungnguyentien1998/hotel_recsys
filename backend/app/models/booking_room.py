from django.db import models
from app.models.room import Room
from app.models.booking import Booking
from app.utils.model_maker import BaseModel
from django.conf import settings


class BookingRoom(BaseModel):
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)

    # @property
    # def booking_id(self):
    #     return self.booking.uuid
    #
    # @property
    # def room_id(self):
    #     return self.room.uuid

    class Meta:
        db_table = 'booking_room'
