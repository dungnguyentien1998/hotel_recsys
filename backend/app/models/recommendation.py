from django.db import models
from app.models.hotel import Hotel
from app.utils.model_maker import BaseModel


# Recommendation model
class Recommendation(BaseModel):
    similarity = models.FloatField(blank=True)
    hotel = models.ForeignKey(Hotel, related_name='recommendations', on_delete=models.SET_NULL, null=True)
    collation_hotel = models.ForeignKey(Hotel, related_name='collated_recommendations', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'recommendation'
