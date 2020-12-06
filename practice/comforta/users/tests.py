import json
from users.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User
from rest_framework.test import APIClient


class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {"email": "alexei.gordienko@hotmail.com",
                "password": "helloworld13", "password1": "helloworld13"}
        register_url = reverse('register')
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_registration_with_passwords_not_match(self):
        data = {"email": "alexei.gordienko@hotmail.com",
                "password": "hel", "password1": "helloworld13"}
        register_url = reverse('register')
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_bad_email(self):
        data = {"email": "alexei.gordienko",
                "password": "helloworld13", "password1": "helloworld13"}
        register_url = reverse('register')
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_registration_with_bad_serializer(self):
        data = {"emil": "alexei.gordienko",
                "paword": "helloworld13", "password1": "helloworld13"}
        register_url = reverse('register')
        response = self.client.post(register_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LoginTestCase(APITestCase):
    def setUp(self):
        user1 = User.objects.create_user(
            email="alexei.gordienko@hotmail.com", password="helloworld13")

    def test_login(self):
        data1 = {"email": "alexei.gordienko@hotmail.com",
                 "password": "helloworld13"}
        login_url = reverse('login')
        response1 = self.client.post(login_url, data1)
        self.assertEqual(response1.status_code, status.HTTP_200_OK)

    def test_login_with_bad_request(self):
        data1 = {"email": "alexei.gordienko@hotmail.com",
                 "password": "heworld13"}
        login_url = reverse('login')
        response1 = self.client.post(login_url, data1)
        self.assertEqual(response1.status_code, status.HTTP_401_UNAUTHORIZED)


class ViewTestCase(APITestCase):
    def test_View(self):
        client = APIClient()
        user = User.objects.create_user(
            email="alexei.gordienko@hotmail.com", password="helloworld13")
        user1 = User.objects.get(email="alexei.gordienko@hotmail.com")
        user1.Role = 'Admin'
        client.force_authenticate(user=user1)
        all_url = reverse('all')
        response = client.get(all_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_View_without_admin_rights(self):
        client = APIClient()
        user = User.objects.create_user(
            email="alexei.gordienko@hotmail.com", password="helloworld13")
        user1 = User.objects.get(email="alexei.gordienko@hotmail.com")
        client.force_authenticate(user=user1)
        all_url = reverse('all')
        response = client.get(all_url)

        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)


class DeleteTestCase(APITestCase):
    def test_Delete(self):
        client = APIClient()
        user = User.objects.create_user(
            email="alexei.gordienko@hotmail.com", password="helloworld13")
        user = User.objects.create_user(
            email="axe@mail.ru", password="helloworld13")
        user1 = User.objects.get(email="alexei.gordienko@hotmail.com")
        user1.Role = 'Admin'
        client.force_authenticate(user=user1)
        user2 = User.objects.get(email="axe@mail.ru")
        userPK = user2.id
        all_url = reverse('delete-user', args=[userPK])
        response = client.delete(all_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_Delete_with_wrong_pk(self):
        client = APIClient()
        user = User.objects.create_user(
            email="alexei.gordienko@hotmail.com", password="helloworld13")
        user = User.objects.create_user(
            email="axe@mail.ru", password="helloworld13")
        user1 = User.objects.get(email="alexei.gordienko@hotmail.com")
        user1.Role = 'Admin'
        client.force_authenticate(user=user1)
        userPK = 9
        all_url = reverse('delete-user', args=[userPK])
        response = client.delete(all_url)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_Delete_without_admin_rights(self):
        client = APIClient()
        user = User.objects.create_user(
            email="alexei.gordienko@hotmail.com", password="helloworld13")
        user = User.objects.create_user(
            email="axe@mail.ru", password="helloworld13")
        user1 = User.objects.get(email="alexei.gordienko@hotmail.com")
        client.force_authenticate(user=user1)
        userPK = 9
        all_url = reverse('delete-user', args=[userPK])
        response = client.delete(all_url)

        self.assertEqual(response.status_code,
                         status.HTTP_405_METHOD_NOT_ALLOWED)
