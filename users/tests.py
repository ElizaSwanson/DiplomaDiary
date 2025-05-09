from django.test import TestCase
from django.urls import reverse

from .models import User


class UserViewsTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="test@mail.com",
            password="test12345",
            is_active=False,
        )
        self.login_url = reverse("users:login")
        self.register_url = reverse("users:register")

    def test_login_view(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "login.html")

    def test_user_registration_view(self):
        response = self.client.post(
            self.register_url,
            {
                "email": "new@test.ru",
                "username": "testusername",
                "password1": "pass12345",
                "password2": "pass12345",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email="new@test.ru").exists())
