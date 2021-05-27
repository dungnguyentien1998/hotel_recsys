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

    @property
    def complaint_title(self):
        return self.complaint.title

    @property
    def complaint_content(self):
        return self.complaint.content

    @property
    def complaint_image(self):
        return self.complaint.image.url

    @property
    def complaint_created(self):
        return self.complaint.created

    @property
    def hotel_name(self):
        return self.complaint.hotel.name

    @property
    def owner_name(self):
        return self.complaint.hotel.owner_name

    @property
    def owner_tel(self):
        return self.complaint.hotel.owner_tel

    @property
    def owner_email(self):
        return self.complaint.hotel.owner_email

    class Meta:
        db_table = 'reply'
