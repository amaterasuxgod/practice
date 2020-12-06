from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.contrib.auth.models import User


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if email is None:
            raise TypeError('Users should have an Email')
        if password is None:
            raise TypeError('Password should not be none')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    IsConfirmed = models.BooleanField(null=False, default=False)
    Roles = [('Admin', 'Admin'), ('User', 'User')]
    Role = models.CharField(max_length=20, null=False,
                            choices=Roles, default="User")
    DateCreated = models.DateField(null=False, auto_now_add=True)
    DateUpdated = models.DateField(null=False, auto_now=True)

    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def IsAdmin(self):
        if self.Role == 'Admin':
            return True
        return False
