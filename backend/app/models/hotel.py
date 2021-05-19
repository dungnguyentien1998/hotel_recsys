from django.conf import settings
from django.db import models
from app.models.user import User
from app.utils.model_maker import BaseModel
from django.contrib.postgres.fields import ArrayField


# Amenity model
class HotelAmenity(models.TextChoices):
    FREE_PARKING = 'free parking'
    FITNESS_CENTER = 'fitness center'
    FREE_BREAKFAST = 'free breakfast'
    SWIMMING_POOL = 'swimming pool'


# Hotel model
class Hotel(BaseModel):
    name = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    star = models.PositiveIntegerField(blank=True)
    city = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    district = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    ward = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    address = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN, null=True)
    image = models.ImageField(blank=True)
    amenities = ArrayField(models.CharField(max_length=settings.CHAR_FIELD_MAX_LEN, choices=HotelAmenity.choices))
    user = models.ForeignKey(User, related_name='hotels', on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(default=False)

    @property
    def owner_name(self):
        return self.user.name

    @property
    def owner_tel(self):
        return self.user.tel

    @property
    def owner_email(self):
        return self.user.email

    @property
    def num_rooms(self):
        return len(self.rooms.all())

    @property
    def num_complaints(self):
        return len(self.complaints.all())

    @property
    def num_reviews(self):
        return len(self.reviews.all())

    @property
    def rating(self):
        reviews = self.reviews.all()
        sum = 0
        for review in reviews:
            sum = sum + review.rating

        if len(reviews) == 0:
            return 0
        else:
            return round(sum/len(reviews), 1)

    class Meta:
        db_table = 'hotel'
