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
    class Meta:
        model = Reply
        fields = Reply.get_fields()
