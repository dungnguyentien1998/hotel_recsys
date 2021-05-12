from rest_framework.response import Response
from rest_framework.views import APIView
from app import models
from app.serializers import FavoriteSerializer, FavoriteDetailSerializer
from app.utils.serializer_validator import validate_serializer


class Favorite(APIView):
    permission_classes = ()

    # List favorites
    def get(self, request):
        user = request.user
        favorites = models.Favorite.objects.filter(user_id=user.uuid, hotel__isnull=False)
        return Response({
            'success': True,
            'favorites': FavoriteDetailSerializer(favorites, many=True).data
        })

    # Create favorites
    def post(self, request, hotel_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        serializer = FavoriteSerializer(data=request.data, context={'user': request.user, 'hotel': hotel})
        validate_serializer(serializer=serializer)
        favorite = serializer.save()
        return Response({
            'success': True,
            'favorite': FavoriteDetailSerializer(favorite).data
        })

    def delete(self, request, favorite_id):
        favorite = models.Favorite.objects.get(uuid=favorite_id)
        favorite.delete()
        return Response({
            'success': True,
            'favorite': FavoriteDetailSerializer(favorite).data
        })


class FavoriteDetail(APIView):
    permission_classes = ()

    # Delete favorites
    def delete(self, request, hotel_id, favorite_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        favorite = models.Favorite.objects.get(uuid=favorite_id, hotel_id=hotel.uuid)
        favorite.delete()
        return Response({
            'success': True,
            'favorite': FavoriteDetailSerializer(favorite).data
        })
