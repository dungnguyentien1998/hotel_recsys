from django.conf import settings
from django.db import models

from app.models import Complaint
from app.models.user import User
from app.models.hotel import Hotel
from app.utils.model_maker import BaseModel


class Reply(BaseModel):
    title = models.CharField(blank=True, max_length=settings.CHAR_FIELD_MAX_LEN)
    image = models.ImageField(null=True)
    content = models.TextField(blank=True, max_length=settings.AREA_FIELD_MAX_LEN)
    # user = models.ForeignKey(User, related_name='replys', on_delete=models.SET_NULL, null=True)
    # hotel = models.ForeignKey(Hotel, related_name='replys', on_delete=models.SET_NULL, null=True)
    complaint = models.ForeignKey(Complaint, related_name='replys', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'reply'
