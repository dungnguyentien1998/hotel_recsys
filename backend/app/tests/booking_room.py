from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from django.urls import reverse, include, path
from app.models import Hotel, User, Booking, Type, Room, BookingRoom


class BookingRoomTestCase(APITestCase, URLPatternsTestCase):
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
        self.booking = Booking.objects.create(
            check_in_time='2021-04-05 09:00:00',
            check_out_time='2021-04-07 09:00:00',
            user=self.user,
            created='2021-04-01 09:00:00',
            updated='2021-04-01 09:00:00',
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
        self.room = Room.objects.create(
            room_number='123',
            image='test',
            hotel=self.hotel,
            type=self.type
        )
        self.booking_room = BookingRoom.objects.create(
            booking=self.booking,
            room=self.room
        )

    urlpatterns = [
        path('api/', include('app.urls')),
    ]

    def test_get_rooms_from_booking(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel.arrange_room', args=[Booking.objects.get(check_in_time='2021-04-05 09:00:00').uuid])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_assign_rooms(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel.arrange_room', args=[Hotel.objects.get(name='test').uuid])
        assign_data = {
            'booking_id': Booking.objects.get(check_in_time='2021-04-05 09:00:00').uuid,
            'room_numbers': [Room.objects.get(room_number='123').uuid]
        }
        response = self.client.post(url, assign_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_new_bookings(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:hotel.new_bookings', args=[Hotel.objects.get(name='test').uuid])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
