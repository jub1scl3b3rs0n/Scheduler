from django.test import TestCase
from django.contrib.auth.models import User
from .models import ServiceProvider, Appointment
from django.utils import timezone

class UserTestCase(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username="testuser", password="12345")
        self.assertEqual(user.username, "testuser")

class AppointmentTestCase(TestCase):
    def setUp(self):
        self.client_user = User.objects.create_user(username="client", password="123")
        self.provider_user = User.objects.create_user(username="provider", password="123")
        self.provider = ServiceProvider.objects.create(user=self.provider_user, bio="Barbeiro")

    def test_create_appointment(self):
        appointment = Appointment.objects.create(
            client=self.client_user,
            provider=self.provider,
            date="2025-08-01",
            time="14:00"
        )
        self.assertEqual(appointment.provider.user.username, "provider")
