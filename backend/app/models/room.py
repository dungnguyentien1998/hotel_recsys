from django.conf import settings
from django.db import models
from app.models.hotel import Hotel
from app.models.type import Type
from app.utils.model_maker import BaseModel


# Room model
class Room(BaseModel):
    room_number = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    image = models.ImageField(blank=True)
    # hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.SET_NULL, null=True)
    # type = models.ForeignKey(Type, related_name='rooms', on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, related_name='rooms', on_delete=models.DO_NOTHING, null=True)
    type = models.ForeignKey(Type, related_name='rooms', on_delete=models.DO_NOTHING, null=True)

    @property
    def capacity(self):
        return self.type.capacity

    @property
    def adult_number(self):
        return self.type.adult_number

    @property
    def children_number(self):
        return self.type.children_number

    @property
    def price(self):
        return self.type.price

    @property
    def amenities(self):
        return self.type.amenities

    @property
    def room_type(self):
        return self.type.name

    @property
    def area(self):
        return self.type.area

    class Meta:
        db_table = 'room'
