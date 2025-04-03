from django.core.cache import cache
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class RateLimitTestCase(TestCase):
    def setUp(self):
        """Set up a test client and a user (if authentication is required)."""
        self.client = APIClient()
        self.url = reverse("rate_limited")
        self.user = get_user_model().objects.create_user(username="testuser", password="password")

        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    def test_rate_limit(self):
        """Ensure that requests beyond the allowed limit are blocked."""
        cache.clear()
        for _ in range(5):
            response = self.client.get(self.url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)
        self.assertEqual(response.json(), {"error": "Rate limit exceeded. Try again later."})
