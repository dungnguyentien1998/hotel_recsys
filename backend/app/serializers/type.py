from app.models import Type
from rest_framework import serializers
from app.exceptions import ValidationError


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = Type.editable_fields()

    def create(self, validated_data):
        validated_data['hotel_id'] = self.context['hotel'].uuid
        current_type = Type.objects.filter(hotel_id=validated_data['hotel_id'], name=validated_data['room_type'])
        if len(current_type) > 0:
            raise ValidationError("Room type " + validated_data['room_type'] + " already existed")
        room_type = Type(**validated_data)
        room_type.save()
        return room_type

    def update(self, instance, validated_data):
        room_type = self.context['type'].name
        if room_type != validated_data['room_type']:
            current_type = Type.objects.filter(hotel_id=self.context['hotel'].uuid, name=validated_data['room_type'])
            if len(current_type) > 0:
                raise ValidationError("Room type " + validated_data['room_type'] + " already existed")
        [setattr(instance, field, value) for field, value in validated_data.items()]
        instance.save()
        return instance


class TypeDetailSerializer(serializers.ModelSerializer):
    images = serializers.ReadOnlyField()

    class Meta:
        model = Type
        fields = [*Type.get_fields(), 'images']
