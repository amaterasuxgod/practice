import json
from users.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Installation
from rest_framework.test import APIClient


class CreateInstallationTestCase(APITestCase):
    def setUp(self):
        User.objects.create_user(
            email="alexei.gordienko@hotmail.com", password="hotmail15")
        user1 = User.objects.get(email="alexei.gordienko@hotmail.com")
        user1.Role = 'Admin'
        self.client.force_authenticate(user=user1)

    def test_create(self):
        data1 = {"nme": "fsgaesg",
                 "description": "first_dgsc", "serial_number": "8957257", "FirmwareVersion": "15t35"}
        create_url = reverse('create')
        response = self.client.post(create_url, data1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
