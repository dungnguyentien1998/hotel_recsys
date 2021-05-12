from rest_framework.response import Response
from rest_framework.views import APIView
from app import models
from app.serializers import ReviewSerializer, ReviewDetailSerializer
from app.permissions.review import ReviewPermission
from app.utils.serializer_validator import validate_serializer


class Review(APIView):
    permission_classes = (ReviewPermission,)

    # List reviews
    def get(self, request, hotel_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        reviews = models.Review.objects.filter(hotel_id=hotel.uuid)
        return Response({
            'success': True,
            'reviews': ReviewDetailSerializer(reviews, many=True).data
        })

    # Create review
    def post(self, request, hotel_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        serializer = ReviewSerializer(data=request.data, context={'user': request.user, 'hotel': hotel})
        validate_serializer(serializer=serializer)
        review = serializer.save()
        return Response({
            'success': True,
            'review': ReviewDetailSerializer(review).data
        })


class ReviewDetail(APIView):
    permission_classes = (ReviewPermission,)

    # Get one review
    def get(self, request, hotel_id, review_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        review = models.Review.objects.get(uuid=review_id, hotel_id=hotel.uuid)
        return Response({
            'success': True,
            'review': ReviewDetailSerializer(review).data
        })

    # Update review
    def put(self, request, hotel_id, review_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        review = models.Review.objects.get(uuid=review_id, hotel_id=hotel.uuid)
        self.check_object_permissions(request=request, obj=review)
        serializer = ReviewSerializer(data=request.data)
        validate_serializer(serializer=serializer)
        review = serializer.update(instance=review, validated_data=serializer.validated_data)
        return Response({
            'success': True,
            'review': ReviewDetailSerializer(review).data
        })

    # Delete review
    def delete(self, request, hotel_id, review_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)
        review = models.Review.objects.get(uuid=review_id, hotel_id=hotel.uuid)
        self.check_object_permissions(request=request, obj=review)
        review.delete()
        return Response({
            'success': True,
            'review': ReviewDetailSerializer(review).data
        })
