from app.models import Favorite
from rest_framework import serializers


# Favorite crud
class FavoriteSerializer(serializers.ModelSerializer):
    # Favorite data
    class Meta:
        model = Favorite
        fields = Favorite.editable_fields()

    def create(self, validated_data):
        # Get user id and hotel id
        validated_data['user_id'] = self.context['user'].uuid
        validated_data['hotel_id'] = self.context['hotel'].uuid
        # Create favorite
        favorite = Favorite(**validated_data)
        favorite.save()
        return favorite

    def update(self, instance, validated_data):
        # Update favorite
        [setattr(instance, field, value) for field, value in validated_data.items()]
        instance.save()
        return instance


class FavoriteDetailSerializer(serializers.ModelSerializer):
    # Favorite data used to represent
    hotelid = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    city = serializers.ReadOnlyField()
    district = serializers.ReadOnlyField()
    ward = serializers.ReadOnlyField()
    address = serializers.ReadOnlyField()
    image = serializers.ReadOnlyField()
    num_rooms = serializers.ReadOnlyField()
    num_complaints = serializers.ReadOnlyField()
    num_reviews = serializers.ReadOnlyField()
    rating = serializers.ReadOnlyField()
    star = serializers.ReadOnlyField()

    class Meta:
        model = Favorite
        fields = [*Favorite.get_fields(), 'hotelid', 'name', 'city', 'district',
                  'ward', 'address', 'image', 'num_rooms', 'num_complaints', 'num_reviews', 'rating', 'star']
