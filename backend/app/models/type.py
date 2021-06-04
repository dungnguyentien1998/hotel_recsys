from django.conf import settings
from django.db import models
from app.models import Hotel
from app.utils.model_maker import BaseModel
from django.contrib.postgres.fields import ArrayField


# Amenity model
class RoomAmenity(models.TextChoices):
    BATHROBES = 'bathrobes'
    COFFEE_KIT = 'coffee kit'
    CLOTHES_RACK = 'clothes rack'
    WIFI = 'wifi'
    TISSUE_BOX = 'tissue box'
    TOILETRIES = 'toiletries'
    BATHTUB = 'bathtub'
    REFRIGERATOR = 'refrigerator'
    HAIR_DRYER = 'hair dryer'
    ELECTRIC_KETTLE = 'electric kettle'


class Type(BaseModel):
    name = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    capacity = models.IntegerField(default=1)
    adult_number = models.IntegerField(default=1)
    children_number = models.IntegerField(default=0)
    price = models.IntegerField(blank=True)
    area = models.IntegerField(blank=True)
    amenities = ArrayField(models.CharField(max_length=settings.CHAR_FIELD_MAX_LEN, choices=RoomAmenity.choices),
                           blank=True)
    # hotel = models.ForeignKey(Hotel, related_name='types', on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, related_name='types', on_delete=models.DO_NOTHING, null=True)

    def images(self):
        from app.models import Room
        rooms = Room.objects.filter(type_id=self.uuid)
        images = []
        for room in rooms:
            image = room.image.url
            images.append(image)
        return images

    class Meta:
        db_table = 'type'
