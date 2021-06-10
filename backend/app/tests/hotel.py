from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from django.urls import reverse, include, path
from app.models import Hotel, User


class HotelTestCase(APITestCase, URLPatternsTestCase):
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

    urlpatterns = [
        path('api/', include('app.urls')),
    ]

    def test_create_hotel_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel')
        hotel_data = {
            'name': 'test1',
        }
        response = self.client.post(url, hotel_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_hotels_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_hotel_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel.detail', args=[Hotel.objects.get(name='test').uuid])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_hotel_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel.detail', args=[Hotel.objects.get(name='test').uuid])
        hotel_data = {
            'name': 'new_test',
            'city': 'test',
            'district': 'test',
            'ward': 'test',
            'address': 'test',
            'amenities': 'free parking'
        }
        response = self.client.put(url, hotel_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, {'name': 'new_test'})

    def test_delete_hotel_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel.detail', args=[Hotel.objects.get(name='test').uuid])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_activate_hotel(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel.manage', args=[Hotel.objects.get(name='test').uuid])
        hotel_data = {
            'is_active': True
        }
        response = self.client.put(url, hotel_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_hotel_notification(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:notification.hotel')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
