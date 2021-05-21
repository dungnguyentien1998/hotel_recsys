from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from django.urls import reverse, include, path
from app.models import Hotel, User, Review


class ReviewTestCase(APITestCase, URLPatternsTestCase):
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
        self.review = Review.objects.create(
            title='test',
            content='test',
            rating=5,
            user=self.user,
            hotel=self.hotel
        )

    urlpatterns = [
        path('api/', include('app.urls')),
    ]

    def test_create_review_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:review', args=[Hotel.objects.get(name='test').uuid])
        review_data = {
            'title': 'test1',
            'content': 'test1',
            'rating': 4
        }
        response = self.client.post(url, review_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_reviews_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:review', args=[Hotel.objects.get(name='test').uuid])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_review_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:review.detail', args=[Hotel.objects.get(name='test').uuid, Review.objects.get(title='test').uuid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_review_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:review.detail', args=[Hotel.objects.get(name='test').uuid, Review.objects.get(title='test').uuid])
        review_data = {
            'title': 'new_test',
            'content': 'new_test',
            'rating': 4
        }
        response = self.client.put(url, review_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(response.data, {'name': 'new_test'})

    def test_delete_review_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:review.detail', args=[Hotel.objects.get(name='test').uuid, Review.objects.get(title='test').uuid])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
