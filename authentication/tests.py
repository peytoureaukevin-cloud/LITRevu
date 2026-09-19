"""Tests de l'application d'authentification."""

from django.test import TestCase
from django.urls import reverse

from .models import User


class AuthenticationTests(TestCase):
    def test_signup_creates_and_authenticates_user(self):
        response = self.client.post(
            reverse("signup"),
            {
                "username": "nouveau_lecteur",
                "password1": "MotDePasse!123",
                "password2": "MotDePasse!123",
            },
        )

        self.assertRedirects(response, reverse("home"))
        self.assertTrue(User.objects.filter(username="nouveau_lecteur").exists())
        self.assertTrue(response.wsgi_request.user.is_authenticated)
