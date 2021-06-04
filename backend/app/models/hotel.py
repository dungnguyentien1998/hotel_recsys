from django.conf import settings
from django.db import models
from app.models.user import User
from app.utils.model_maker import BaseModel
from django.contrib.postgres.fields import ArrayField
from enum import Enum


# Amenity model
class HotelAmenity(models.TextChoices):
    FREE_PARKING = 'free parking'
    FITNESS_CENTER = 'fitness center'
    BREAKFAST = 'breakfast'
    SWIMMING_POOL = 'swimming pool'
    BAR = 'bar'
    SPA = 'spa'
    ROOM_SERVICE = 'room service'
    NON_SMOKING_ICON = 'non smoking icon'


class Status(models.TextChoices):
    ACTIVE = 'active'
    REJECT = 'reject'
    PENDING = 'pending'

    def __eq__(self, other):
        if isinstance(other, Enum):
            super.__eq__(self, other)
        else:
            return self.value == other


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
    status = models.CharField(max_length=8, choices=Status.choices, default=Status.PENDING)
    reject_reason = models.CharField(null=True, max_length=settings.CHAR_FIELD_MAX_LEN)

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

    @property
    def num_new_bookings(self):
        from app.models.booking import Booking
        from app.models.booking_room import BookingRoom
        bookings = Booking.objects.filter(hotel_id=self.uuid)
        count = 0
        for booking in bookings:
            booking_rooms = BookingRoom.objects.filter(booking_id=booking.uuid)
            if len(booking_rooms) <= 0:
                count = count + 1

        return count

    class Meta:
        db_table = 'hotel'
