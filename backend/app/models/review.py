from django.conf import settings
from django.db import models
from app.models.user import User
from app.models.hotel import Hotel
from app.utils.model_maker import BaseModel


# Review model
class Review(BaseModel):
    rating = models.PositiveIntegerField(blank=True)
    title = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    content = models.TextField(blank=True, max_length=settings.AREA_FIELD_MAX_LEN)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, related_name='reviews', on_delete=models.SET_NULL, null=True)

    # User who makes review
    @property
    def user_name(self):
        return self.user.name

    class Meta:
        db_table = 'review'
