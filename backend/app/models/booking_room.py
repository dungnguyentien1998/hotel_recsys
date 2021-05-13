from django.db import models
from app.models.room import Room
from app.models.booking import Booking
from app.utils.model_maker import BaseModel
from django.conf import settings


class BookingRoom(BaseModel):
    booking = models.ForeignKey(Booking, on_delete=models.DO_NOTHING, null=True)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'booking_room'
