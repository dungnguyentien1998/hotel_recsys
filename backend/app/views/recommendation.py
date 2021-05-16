from rest_framework.response import Response
from rest_framework.views import APIView
import random
from app import models
from app.serializers import HotelDetailSerializer


class Recommendation(APIView):
    permission_classes = ()

    # Recommend used when logged in
    def get(self, request):
        user = request.user
        favorites = models.Favorite.objects.filter(user_id=user.uuid, hotel__isnull=False)
        if not favorites.count():
            # reviews = models.Review.objects.filter(user_id=user.uuid, hotel__isnull=False)
            # if not reviews.count():
            #     return Response({
            #         'success': True,
            #         'recommendationsLogin': []
            #     })
            # max_rating = 1
            # for review in reviews:
            #     if review.rating > max_rating:
            #         max_rating = review.rating
            # max_reviews = models.Review.objects.filter(user_id=user.uuid, rating=max_rating, hotel__isnull=False)
            # hotel = random.choice(max_reviews).hotel
            return Response({
                'success': True,
                'recommendationsLogin': []
            })

        num_recommend = 6
        favorites_ids = []
        for favorite in favorites:
            favorites_ids.append(favorite.hotel.uuid)

        total_predictions = []
        count = 0
        for favorite in favorites:
            hotel = favorite.hotel
            single_predictions = []

            first_recommend = models.Recommendation.objects.filter(hotel_id=hotel.uuid)
            for tmp_recommend in first_recommend:
                hotel_id = tmp_recommend.collation_hotel.uuid
                if hotel_id not in favorites_ids:
                    tup = [hotel_id, tmp_recommend.similarity]
                    single_predictions.append(tup)
                    if count == 0:
                        total_tup = [hotel_id, 0]
                        total_predictions.append(total_tup)

            second_recommend = models.Recommendation.objects.filter(collation_hotel_id=hotel.uuid)
            for tmp_recommend in second_recommend:
                hotel_id = tmp_recommend.hotel.uuid
                if hotel_id not in favorites_ids:
                    tup = [hotel_id, tmp_recommend.similarity]
                    single_predictions.append(tup)
                    if count == 0:
                        total_tup = [hotel_id, 0]
                        total_predictions.append(total_tup)

            for i in range(len(single_predictions)):
                current_sum = total_predictions[i][1]
                current_sum = current_sum + single_predictions[i][1]
                total_predictions[i][1] = current_sum

            count = count + 1

        predictions = []
        for prediction in total_predictions:
            temp = tuple(prediction)
            predictions.append(temp)

        # Sorting based on similarity points
        predictions.sort(key=lambda tup: tup[1], reverse=True)

        if not predictions:
            return Response({
                'success': True,
                'recommendationsLogin': []
            })

        recommend_hotels = []
        counter = 0
        i = 0
        while counter < num_recommend and i < len(predictions):
            hotel = models.Hotel.objects.get(uuid=predictions[i][0])
            reviews = models.Review.objects.filter(hotel_id=hotel.uuid, user_id=request.user.uuid)
            if reviews.count() <= 0:
                counter = counter + 1
                recommend_hotels.append(hotel)
            i = i + 1

        if not recommend_hotels:
            return Response({
                'success': True,
                'recommendationsLogin': []
            })

        return Response({
            'success': True,
            'recommendationsLogin': HotelDetailSerializer(recommend_hotels, many=True).data
        })


class RecommendationDetail(APIView):
    permission_classes = ()

    # Recommend used for hotel detail
    def get(self, request, hotel_id):
        hotel = models.Hotel.objects.get(uuid=hotel_id)

        num_recommend = 6
        predictions = []

        first_recommend = models.Recommendation.objects.filter(hotel_id=hotel.uuid)
        for tmp_recommend in first_recommend:
            tup = (tmp_recommend.collation_hotel.uuid, tmp_recommend.similarity)
            predictions.append(tup)

        second_recommend = models.Recommendation.objects.filter(collation_hotel_id=hotel.uuid)
        for tmp_recommend in second_recommend:
            tup = (tmp_recommend.hotel.uuid, tmp_recommend.similarity)
            predictions.append(tup)

        # Sorting based on similarity points
        predictions.sort(key=lambda tup: tup[1], reverse=True)

        if not predictions:
            return Response({
                'success': True,
                'recommendations': []
            })

        recommend_hotels = []
        counter = 0
        i = 0
        while counter < num_recommend and i < len(predictions):
            hotel = models.Hotel.objects.get(uuid=predictions[i][0])
            reviews = models.Review.objects.filter(hotel_id=hotel.uuid, user_id=request.user.uuid)
            if reviews.count() <= 0:
                counter = counter + 1
                recommend_hotels.append(hotel)
            i = i + 1

        if not recommend_hotels:
            return Response({
                'success': True,
                'recommendations': []
            })

        return Response({
            'success': True,
            'recommendations': HotelDetailSerializer(recommend_hotels, many=True).data
        })
