from django.db import models
from app.models.type import Type
from app.models.booking import Booking
from app.utils.model_maker import BaseModel
from django.conf import settings


class BookingType(BaseModel):
    booking = models.ForeignKey(Booking, on_delete=models.DO_NOTHING, null=True)
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, null=True)
    count = models.IntegerField(blank=True)

    class Meta:
        db_table = 'booking_type'
