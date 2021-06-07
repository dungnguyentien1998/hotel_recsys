from rest_framework.response import Response
from rest_framework.views import APIView
from app import models
from app.serializers import TypeSerializer, TypeDetailSerializer
from app.utils.serializer_validator import validate_serializer


class Type(APIView):
    permission_classes = ()

    def get(self, request, hotel_id):
        types = models.Type.objects.filter(hotel_id=hotel_id)
        return Response({
            'success': True,
            'types': TypeDetailSerializer(types, many=True).data
        })

    def post(self, request, hotel_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        serializer = TypeSerializer(data=request.data, context={'hotel': hotel})
        validate_serializer(serializer=serializer)
        room_type = serializer.save()
        return Response({
            'success': True,
            'type': TypeDetailSerializer(room_type).data
        })


class TypeDetail(APIView):
    permission_classes = ()

    def put(self, request, hotel_id, type_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        room_type = models.Type.objects.get(uuid=type_id)
        serializer = TypeSerializer(data=request.data, context={'hotel': hotel, 'type': room_type})
        validate_serializer(serializer=serializer)
        serializer.update(instance=room_type, validated_data=serializer.validated_data)
        return Response({
            'success': True,
            'type': TypeDetailSerializer(room_type).data
        })

    def delete(self, request, hotel_id, type_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        room_type = models.Type.objects.get(uuid=type_id)
        room_type.delete()
        return Response({
            'success': True,
            'type': TypeDetailSerializer(room_type).data
        })

