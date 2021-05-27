from app.models import Reply
from rest_framework import serializers


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = Reply.editable_fields()

    def create(self, validated_data):
        # validated_data['user_id'] = self.context['user'].uuid
        validated_data['complaint_id'] = self.context['complaint'].uuid
        reply = Reply(**validated_data)
        reply.save()
        return reply


class ReplyDetailSerializer(serializers.ModelSerializer):
    complaint_title = serializers.ReadOnlyField()
    complaint_content = serializers.ReadOnlyField()
    complaint_image = serializers.ReadOnlyField()
    complaint_created = serializers.ReadOnlyField()
    hotel_name = serializers.ReadOnlyField()
    owner_name = serializers.ReadOnlyField()
    owner_tel = serializers.ReadOnlyField()
    owner_email = serializers.ReadOnlyField()

    class Meta:
        model = Reply
        fields = [*Reply.get_fields(), 'complaint_title', 'complaint_content', 'complaint_image', 'complaint_created',
                  'hotel_name', 'owner_name', 'owner_tel', 'owner_email']
