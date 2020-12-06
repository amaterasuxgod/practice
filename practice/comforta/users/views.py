from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import mixins
from .serializers import RegisterSerializer, UserSerializer, LoginSerializer
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from django.conf import settings
from rest_framework.generics import GenericAPIView
from .models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import authenticate, login
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import update_last_login
import json
# Create your views here.


@api_view(['POST'])
def Register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def Login(request):
    serializer = LoginSerializer(data=request.data)
    try:
        serializer.is_valid()
        username = serializer.data['email']
        password = serializer.data['password']
        user = authenticate(username=username, password=password)
    except:
        return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
    if not user == None:
        user_logged_in.disconnect(
            update_last_login, dispatch_uid='update_last_login')
        login(request, user)
        return Response('Login', status=status.HTTP_200_OK)
    else:
        return Response('Login failed', status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def AllUsersView(request):
    if request.user.IsAdmin:
        paginator = PageNumberPagination()
        paginator.page_size = 10
        Users = User.objects.all()
        result_page = paginator.paginate_queryset(Users, request)
        serializer = UserSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    return Response('You must have admin rights to access to this page', status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def DeleteUserView(request, pk):
    if request.user.IsAdmin:
        try:
            rm_user = User.objects.get(id=pk)
            rm_user.delete()
            return Response({'detail': 'User was deleted'}, status=status.HTTP_200_OK)
        except:
            return Response('Wrong primary key', status=status.HTTP_400_BAD_REQUEST)
    return Response('You must have admin rights to access to this page', status=status.HTTP_405_METHOD_NOT_ALLOWED)
