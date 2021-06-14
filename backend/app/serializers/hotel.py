from app.exceptions import ValidationError
from app.models import Hotel, Status
from rest_framework import serializers
from django.db.models import Q


# Hotel crud
class HotelSerializer(serializers.ModelSerializer):
    # Hotel data
    class Meta:
        model = Hotel
        fields = Hotel.editable_fields()

    def create(self, validated_data):
        # Get user id
        hotels = Hotel.objects.filter(Q(status=Status.ACTIVE) | Q(status=Status.PENDING), email=validated_data['email'])
        if len(hotels) > 0:
            raise ValidationError('Email already exists')
        validated_data['user_id'] = self.context['request'].user.uuid
        # Create hotel
        hotel = Hotel(**validated_data)
        hotel.save()
        return hotel

    def update(self, instance, validated_data):
        # Update hotel
        if validated_data['email']:
            hotels = Hotel.objects.filter(Q(status=Status.ACTIVE) | Q(status=Status.PENDING), email=validated_data['email'])
            if len(hotels) > 0:
                raise ValidationError('Email already exists')
        [setattr(instance, field, value) for field, value in validated_data.items()]
        instance.save()


class HotelierHotelDetailSerializer(serializers.ModelSerializer):
    # Hotel data used to represent, used for hotelier
    num_rooms = serializers.ReadOnlyField()
    num_complaints = serializers.ReadOnlyField()
    num_reviews = serializers.ReadOnlyField()
    rating = serializers.ReadOnlyField()
    num_new_bookings = serializers.ReadOnlyField()

    class Meta:
        model = Hotel
        fields = [*Hotel.get_fields(), 'num_rooms', 'num_complaints', 'num_reviews', 'rating', 'num_new_bookings']


class HotelDetailSerializer(serializers.ModelSerializer):
    # Hotel data used to represent, used for user
    # num_rooms = serializers.ReadOnlyField()
    # num_complaints = serializers.ReadOnlyField()
    # num_reviews = serializers.ReadOnlyField()
    rating = serializers.ReadOnlyField()
    owner_name = serializers.ReadOnlyField()
    owner_tel = serializers.ReadOnlyField()
    owner_email = serializers.ReadOnlyField()

    class Meta:
        model = Hotel
        fields = [*Hotel.get_fields(), 'rating', 'owner_name', 'owner_tel', 'owner_email']
        # fields = [*Hotel.get_fields(), 'num_rooms', 'num_complaints', 'num_reviews', 'rating', 'owner_name',
        #           'owner_tel', 'owner_email']


class HotelActiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        # fields = ['is_active']
        fields = ['status', 'reject_reason']

    def update(self, instance, validated_data):
        [setattr(instance, field, value) for field, value in validated_data.items()]
        instance.save()
        return instance
