from django.contrib.auth import backends
from django.contrib.auth.hashers import check_password
from .models import User


class AuthCustom(backends.ModelBackend):
    def authenticate(self, request, username=None, password=None):
        login_valid = (User.objects.get(email=username).email == username)
        pwd_valid = check_password(
            password, User.objects.get(email=username).password)
        if login_valid and pwd_valid:
            user = User.objects.get(email=username)
            return user
        return None

    def get_user(self, id):
        return User.objects.get(id=id)
