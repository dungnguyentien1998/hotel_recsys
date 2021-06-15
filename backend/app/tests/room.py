from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from django.urls import reverse, include, path
from app.models import Hotel, User, Room, Type


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
            star=2,
            city='test',
            district='test',
            ward='test',
            address='test',
            amenities=['free parking'],
            image='test',
            user=self.user
        )
        self.type = Type.objects.create(
            name='test',
            price=1,
            area=10,
            amenities=['personal care'],
            hotel=self.hotel
        )
        self.room = Room.objects.create(
            room_number='123',
            image='test',
            hotel=self.hotel,
            type=self.type
        )

    urlpatterns = [
        path('api/', include('app.urls')),
    ]

    def test_create_room_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:room', args=[Hotel.objects.get(name='test').uuid])
        room_data = {
            'room_type': 'test',
            'room_numbers': ['123', '456'],
            'images': ['test', 'test']
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
            'room_number': '456',
            'image': 'test',
        }
        response = self.client.put(url, room_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, {'name': 'new_test'})

    def test_delete_room_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:room.detail', args=[Hotel.objects.get(name='test').uuid, Room.objects.get(room_number='123').uuid])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
