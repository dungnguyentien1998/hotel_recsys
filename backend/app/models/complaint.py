from django.conf import settings
from django.db import models
from app.models.user import User
from app.models.hotel import Hotel
from app.utils.model_maker import BaseModel


# Complaint model
class Complaint(BaseModel):
    title = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    image = models.ImageField(null=True)
    content = models.TextField(blank=True, max_length=settings.AREA_FIELD_MAX_LEN)
    user = models.ForeignKey(User, related_name='complaints', on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, related_name='complaints', on_delete=models.SET_NULL, null=True)
    is_processed = models.BooleanField(default=False)

    @property
    def user_name(self):
        return self.user.name

    @property
    def email(self):
        return self.user.email

    class Meta:
        db_table = 'complaint'
