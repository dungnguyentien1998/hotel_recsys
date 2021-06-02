from app.models import Review
from rest_framework import serializers


# Review crud
class ReviewSerializer(serializers.ModelSerializer):
    # Review data
    class Meta:
        model = Review
        fields = Review.editable_fields()

    def create(self, validated_data):
        # Get user id and hotel id
        validated_data['user_id'] = self.context['user'].uuid
        validated_data['hotel_id'] = self.context['hotel'].uuid
        # Create review
        review = Review(**validated_data)
        review.save()
        return review

    def update(self, instance, validated_data):
        # Update review
        [setattr(instance, field, value) for field, value in validated_data.items()]
        instance.save()
        return instance


class ReviewDetailSerializer(serializers.ModelSerializer):
    # Review data used to represent
    user_name = serializers.ReadOnlyField()
    owner_id = serializers.ReadOnlyField()

    class Meta:
        model = Review
        fields = [*Review.get_fields(), 'user_name', 'owner_id']
