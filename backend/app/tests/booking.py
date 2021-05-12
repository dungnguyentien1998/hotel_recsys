from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from django.urls import reverse, include, path
from app.models import User, Room, Booking


class BookingTestCase(APITestCase, URLPatternsTestCase):
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
        self.room = Room.objects.create(
            room_type='double',
            capacity=7,
            room_number='123',
            price='123',
            amenities=['wifi'],
            image='test',
        )
        self.booking = Booking.objects.create(
            check_in_time='2021-04-05 09:00:00',
            check_out_time='2021-04-07 09:00:00',
            user=self.user,
            room=self.room
        )

    urlpatterns = [
        path('api/', include('app.urls')),
    ]

    def test_create_booking_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:booking')
        room_id = Room.objects.get(room_number='123').uuid
        booking_data = {
            'check_in_time': '2021-04-10 09:00:00',
            'check_out_time': '2021-04-12 09:00:00',
            'room_id': room_id
        }
        response = self.client.post(url, booking_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_bookings_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:booking')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_booking_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:booking.detail', args=[Booking.objects.get(check_in_time='2021-04-05 09:00:00').uuid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_booking_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:booking.detail', args=[Booking.objects.get(check_in_time='2021-04-05 09:00:00').uuid])
        booking_data = {
            'check_in_time': '2021-04-14 09:00:00',
            'check_out_time': '2021-04-16 09:00:00',
        }
        response = self.client.put(url, booking_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, {'name': 'new_test'})

    def test_delete_booking_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:booking.detail', args=[Booking.objects.get(check_in_time='2021-04-05 09:00:00').uuid])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
