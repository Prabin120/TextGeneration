from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from user.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class GenerateSummaryTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Generate token for the user
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client = APIClient()
        self.url = reverse('generate-summary')

    def test_generate_summary_success(self):
        # Set the Authorization header with the Bearer token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        data = {'text': 'This is a test input for summary generation.'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('result', response.data)

    def test_generate_summary_no_authentication(self):
        # Attempt to access without authentication
        data = {'text': 'This is a test input for summary generation.'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_generate_summary_no_input_text(self):
        # Set the Authorization header with the Bearer token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class GenerateBulletPointsTest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)
        self.client = APIClient()
        self.url = reverse('generate-bullet-points')

    def test_generate_bullet_points_success(self):
        # Set the Authorization header with the Bearer token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        data = {'text': 'This is a test input for bullet points generation.'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('result', response.data)

    def test_generate_bullet_points_no_authentication(self):
        # Attempt to access without authentication
        data = {'text': 'This is a test input for bullet points generation.'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_generate_bullet_points_no_input_text(self):
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)
        response = self.client.post(self.url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
