from rest_framework import serializers
from .models import User
from re import match
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'IsConfirmed',
                  'Role', 'DateCreated', 'DateUpdated']

    def viewall(self):
        return User.objects.all()


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'password1']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = User(email=self.validated_data['email'])

        password = self.validated_data['password']
        password1 = self.validated_data['password1']

        if not password.isalnum():
            raise serializers.ValidationError(
                'Use characters and numbers in your password')
        if len(password) < 8:
            raise serializers.ValidationError(
                'Your password must have at least 8 chars')
        if password != password1:
            raise serializers.ValidationError(
                {'password': 'passwords must match.'})

        account.set_password(password)
        account.save()
        return account


class LoginSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'password']
