from app.models import Complaint
from rest_framework import serializers


# Complaint crud
class ComplaintSerializer(serializers.ModelSerializer):
    # Complaint data
    class Meta:
        model = Complaint
        fields = Complaint.editable_fields()

    def create(self, validated_data):
        # Get user id and hotel id
        validated_data['user_id'] = self.context['user'].uuid
        validated_data['hotel_id'] = self.context['hotel'].uuid
        # Create complaint
        complaint = Complaint(**validated_data)
        complaint.save()
        return complaint


class ComplaintDetailSerializer(serializers.ModelSerializer):
    # Complaint data used to represent
    user_name = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()

    class Meta:
        model = Complaint
        fields = [*Complaint.get_fields(), 'user_name', 'email']
