from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient
from django.urls import reverse, include, path
from app.models import User


class UserTestCase(APITestCase, URLPatternsTestCase):
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
            role='admin',
            birthday='2004-12-26'
        )

    urlpatterns = [
        path('api/', include('app.urls')),
    ]

    def test_register_api(self):
        url = reverse('app:user.register')
        user_data = {
            'email': 'test123@hotmail.com',
            'password': '123456',
            'name': 'Peggy Holt',
            'tel': '0750014613',
            'city': 'test',
            'district': 'test',
            'ward': 'test',
            'address': 'test',
            'role': 'hotelier',
            'birthday': '2004-12-26'
        }
        response = self.client.post(url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_api(self):
        url = reverse('app:user.login')
        user_data = {
            'email': 'danielnorman@hotmail.com',
            'password': '123456',
        }
        response = self.client.post(url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_profile_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:user.account')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_profile_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:user.account')
        user_data = {
            'name': 'new test',
            'tel': '0750014613',
            'city': 'new test',
            'district': 'new test',
            'ward': 'new test',
            'address': 'new test',
            'birthday': '2004-12-26'
        }
        response = self.client.put(url, user_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_users_api(self):
        self.client.force_authenticate(self.user)
        url = reverse('app:user.manage')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

