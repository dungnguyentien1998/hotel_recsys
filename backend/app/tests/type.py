from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from django.urls import reverse, include, path
from app.models import Hotel, Type, User


class TypeTestCase(APITestCase, URLPatternsTestCase):
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
            role='user',
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
        )
        self.type = Type.objects.create(
            name='test',
            price=1,
            area=10,
            amenities=['personal care'],
            hotel=self.hotel
        )

    urlpatterns = [
        path('api/', include('app.urls')),
    ]

    def test_create_type_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:type', args=[Hotel.objects.get(name='test').uuid])
        type_data = {
            'room_type': 'test1',
            'price': 2,
            'area': 10,
            'amenities': 'personal care'
        }
        response = self.client.post(url, type_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_types_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:type', args=[Hotel.objects.get(name='test').uuid])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_type_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:type.detail', args=[Hotel.objects.get(name='test').uuid, Type.objects.get(name='test').uuid])
        type_data = {
            'room_type': 'new_test',
            'price': 3,
            'area': 10,
            'amenities': 'personal care'
        }
        response = self.client.put(url, type_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, {'name': 'new_test'})

    def test_delete_type_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:type.detail', args=[Hotel.objects.get(name='test').uuid, Type.objects.get(name='test').uuid])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
