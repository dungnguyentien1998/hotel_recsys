from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from django.urls import reverse, include, path
from app.models import User, Booking, Hotel, Type, BookingType


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
            capacity=1,
            price=1,
            amenities=['personal care'],
            hotel=self.hotel
        )
        self.booking = Booking.objects.create(
            check_in_time='2021-04-05 09:00:00',
            check_out_time='2021-04-07 09:00:00',
            user=self.user,
            created='2021-04-01 09:00:00',
            updated='2021-04-01 09:00:00',
        )
        self.booking_type = BookingType.objects.create(
            booking=self.booking,
            type=self.type,
            count=1
        )

    urlpatterns = [
        path('api/', include('app.urls')),
    ]

    def test_create_booking_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:booking')
        booking_data = {
            'check_in_time': '2021-04-10 09:00:00',
            'check_out_time': '2021-04-12 09:00:00',
            'hotel_id': Hotel.objects.all()[0].uuid,
            'room_types': [Type.objects.all()[0].name],
            'booking_counts': [1]
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

    def test_delete_booking_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:booking.detail', args=[Booking.objects.get(check_in_time='2021-04-05 09:00:00').uuid])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_bookings_hotelier_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel.bookings', args=[Hotel.objects.all()[0].uuid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_booking_hotelier_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel.booking', args=[Hotel.objects.all()[0].uuid, Booking.objects.get(check_in_time='2021-04-05 09:00:00').uuid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_booking_hotelier_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel.booking', args=[Hotel.objects.all()[0].uuid, Booking.objects.get(check_in_time='2021-04-05 09:00:00').uuid])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
