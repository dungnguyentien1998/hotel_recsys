from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from django.urls import reverse, include, path
from app.models import Hotel, User, Room


class RoomTestCase(APITestCase, URLPatternsTestCase):
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
            city='test',
            district='test',
            ward='test',
            address='test',
            amenities=['free parking'],
            image='test',
            user=self.user
        )
        self.room = Room.objects.create(
            room_type='double',
            capacity=7,
            room_number='123',
            price='123',
            amenities=['wifi'],
            image='test',
            hotel=self.hotel
        )

    urlpatterns = [
        path('api/', include('app.urls')),
    ]

    def test_create_room_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:room', args=[Hotel.objects.get(name='test').uuid])
        room_data = {
            'room_type': 'double',
            'capacity': 7,
            'room_number': '123',
            'price': '123',
        }
        response = self.client.post(url, room_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_rooms_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:room', args=[Hotel.objects.get(name='test').uuid])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_room_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:room.detail', args=[Hotel.objects.get(name='test').uuid, Room.objects.get(room_number='123').uuid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_room_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:room.detail', args=[Hotel.objects.get(name='test').uuid, Room.objects.get(room_number='123').uuid])
        room_data = {
            'room_type': 'single',
            'capacity': 3,
            'room_number': '456',
            'price': '456',
        }
        response = self.client.put(url, room_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, {'name': 'new_test'})

    def test_delete_room_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:room.detail', args=[Hotel.objects.get(name='test').uuid, Room.objects.get(room_number='123').uuid])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
