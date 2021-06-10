from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from django.urls import reverse, include, path
from app.models import Hotel, User, Favorite


class RecommendTestCase(APITestCase, URLPatternsTestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(
            email='danielnorman@hotmail.com',
            password='123456',
            name='Peggy Holt',
            tel='0750014613',
            city='test',
            district='test',
            ward='test',
            address='test',
            role='hotelier',
            birthday='2004-12-26'
        )
        self.hotel = Hotel.objects.create(
            name='test',
            star=2,
            city='test',
            district='test',
            ward='test',
            address='test',
            amenities=['free parking'],
            image='test',
            user=self.user
        )
        self.favorite = Favorite.objects.create(
            user=self.user,
            hotel=self.hotel
        )

    urlpatterns = [
        path('api/', include('app.urls')),
    ]

    def test_get_recommends_detail_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel.recommendations', args=[Hotel.objects.get(name='test').uuid])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_recommends_login_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:recommendations')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
