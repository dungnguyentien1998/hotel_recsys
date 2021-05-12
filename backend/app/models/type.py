from django.conf import settings
from django.db import models
from app.models import Hotel
from app.utils.model_maker import BaseModel
from django.contrib.postgres.fields import ArrayField


# Amenity model
class RoomAmenity(models.TextChoices):
    BATHROBES = 'bathrobes'
    COFFEE_KIT = 'coffee kit'
    PERSONAL_CARE = 'personal care'
    WIFI = 'wifi'
    TISSUE_BOX = 'tissue box'


class Type(BaseModel):
    room_type = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    capacity = models.IntegerField(default=1)
    price = models.IntegerField(blank=True)
    amenities = ArrayField(models.CharField(max_length=settings.CHAR_FIELD_MAX_LEN, choices=RoomAmenity.choices),
                           blank=True)
    # hotel = models.ForeignKey(Hotel, related_name='types', on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, related_name='types', on_delete=models.DO_NOTHING, null=True)

    class Meta:
        db_table = 'type'
