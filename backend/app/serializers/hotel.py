from app.models import Hotel
from rest_framework import serializers


# Hotel crud
class HotelSerializer(serializers.ModelSerializer):
    # Hotel data
    class Meta:
        model = Hotel
        fields = Hotel.editable_fields()

    def create(self, validated_data):
        # Get user id
        validated_data['user_id'] = self.context['request'].user.uuid
        # Create hotel
        hotel = Hotel(**validated_data)
        hotel.save()
        return hotel

    def update(self, instance, validated_data):
        # Update hotel
        [setattr(instance, field, value) for field, value in validated_data.items()]
        instance.save()


class HotelierHotelDetailSerializer(serializers.ModelSerializer):
    # Hotel data used to represent, used for hotelier
    num_rooms = serializers.ReadOnlyField()
    num_complaints = serializers.ReadOnlyField()
    num_reviews = serializers.ReadOnlyField()
    rating = serializers.ReadOnlyField()

    class Meta:
        model = Hotel
        fields = [*Hotel.get_fields(), 'num_rooms', 'num_complaints', 'num_reviews', 'rating']


class HotelDetailSerializer(serializers.ModelSerializer):
    # Hotel data used to represent, used for user
    num_rooms = serializers.ReadOnlyField()
    num_complaints = serializers.ReadOnlyField()
    num_reviews = serializers.ReadOnlyField()
    rating = serializers.ReadOnlyField()

    class Meta:
        model = Hotel
        fields = [*Hotel.get_fields(), 'num_rooms', 'num_complaints', 'num_reviews', 'rating']


class HotelActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ['is_active']

    def update(self, instance, validated_data):
        [setattr(instance, field, value) for field, value in validated_data.items()]
        instance.save()
        return instance
