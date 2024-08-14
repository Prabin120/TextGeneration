from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from django.test import TestCase
from .models import User

class UserAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.login_url = reverse('sign-in')

    def test_user_registration(self):
        response = self.client.post(reverse('user'), {
            'username': 'newuser',
            'password': 'newpass',
            'confirm_password': 'newpass'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 2)

    def test_user_registration_with_same_username(self):
        response = self.client.post(reverse('user'), {
            'username': 'newuser',
            'password': 'newpass',
            'confirm_password': 'newpass2'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_user_registration_with_different_password_and_confirm_password(self):
        response = self.client.post(reverse('user'), {
            'username': 'newuser1',
            'password': 'newpass',
            'confirm_password': 'newpass2'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    
    def test_user_registration_without_confirm_password(self):
        response = self.client.post(reverse('user'), {
            'username': 'newuser1',
            'password': 'newpass',
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(User.objects.count(), 1)

    def test_user_login(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
    
    def test_user_login_with_wrong_password(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass1'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_login_with_wrong_username(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser1',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_user_login_without_password(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser'
        })
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)