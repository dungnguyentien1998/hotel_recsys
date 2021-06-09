from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from django.urls import reverse, include, path
from app.models import Hotel, User, Complaint


class ComplaintTestCase(APITestCase, URLPatternsTestCase):
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
        self.hotelier = User.objects.create(
            email='daniel123@hotmail.com',
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
        )
        self.complaint = Complaint.objects.create(
            title='test',
            content='test',
            image='test',
            user=self.user,
            hotel=self.hotel
        )

    urlpatterns = [
        path('api/', include('app.urls')),
    ]

    def test_create_complaint_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:complaint', args=[Hotel.objects.get(name='test').uuid])
        complaint_data = {
            'title': 'test1',
            'content': 'test1',
            'image': 'test'
        }
        response = self.client.post(url, complaint_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_complaints_api(self):
        self.client.force_authenticate(self.hotelier)
        url = reverse('app:complaint', args=[Hotel.objects.get(name='test').uuid])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_complaint_api(self):
        self.client.force_authenticate(self.hotelier)
        url = reverse('app:complaint.detail', args=[Hotel.objects.get(name='test').uuid, Complaint.objects.get(title='test').uuid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_complaint_api(self):
        self.client.force_authenticate(self.hotelier)
        url = reverse('app:complaint.detail', args=[Hotel.objects.get(name='test').uuid, Complaint.objects.get(title='test').uuid])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_complaint_api(self):
        return None
