from django.db import models
from app.models import User, Hotel
from app.utils.model_maker import BaseModel


# Favorite model
class Favorite(BaseModel):
    user = models.ForeignKey(User, related_name='favorites', on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, related_name='favorites', on_delete=models.SET_NULL, null=True)

    @property
    def hotelid(self):
        return self.hotel.uuid

    @property
    def name(self):
        return self.hotel.name

    @property
    def image(self):
        return self.hotel.image.url

    @property
    def city(self):
        return self.hotel.city

    @property
    def district(self):
        return self.hotel.district

    @property
    def ward(self):
        return self.hotel.ward

    @property
    def address(self):
        return self.hotel.address

    @property
    def num_rooms(self):
        return self.hotel.num_rooms

    @property
    def num_complaints(self):
        return self.hotel.num_complaints

    @property
    def num_reviews(self):
        return self.hotel.num_reviews

    @property
    def rating(self):
        return self.hotel.rating

    @property
    def star(self):
        return self.hotel.star

    class Meta:
        db_table = 'favorite'
