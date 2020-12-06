from django.shortcuts import render
from .models import Installation
from .models import Installation
from .serializers import InstallationSerializer, InstallationViewSerializer, InstForCurrentUserSerializer
from rest_framework.response import Response
from rest_framework import status
from users.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Create(request):
    if request.user.IsAdmin:
        serializer = InstallationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
    return Response('You must have admin rights to access to this page', status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def Delete(request, pk):
    if request.user.IsAdmin:
        try:
            rm_inst = Installation.objects.get(id=pk)
            rm_inst.delete()
            return Response({'detail': 'Installation was deleted'}, status=status.HTTP_200_OK)
        except:
            return Response('Wrong primary key', status=status.HTTP_400_BAD_REQUEST)
    return Response('You must have admin rights to access to this page', status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def Update(request, pk):
    if request.user.IsAdmin:
        try:
            Installations = Installation.objects.get(id=pk)
            serializer = InstallationViewSerializer(
                instance=Installations, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response('Wrong primary key', status=status.HTTP_400_BAD_REQUEST)
    return Response('You must have admin rights to access to this page', status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def View(request):
    if request.user.IsAdmin:
        paginator = PageNumberPagination()
        paginator.page_size = 10
        queryset = Installation.objects.all()
        result = paginator.paginate_queryset(queryset, request)
        serializer = InstallationViewSerializer(result, many=True)
        return paginator.get_paginated_response(serializer.data)
    return Response('You must have admin rights to access to this page', status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def UserView(request):
    cur_count = Installation.objects.filter(owner=request.user)
    if cur_count.count() < 1:
        return Response('You have no installations on your account', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InstForCurrentUserSerializer(cur_count, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UserConnect(request, pk):
    cur_count = Installation.objects.filter(owner=request.user)
    if cur_count.count() > 0:
        return Response('Already own installation')
    else:
        try:
            inst = Installation.objects.get(UIN=pk)
            if inst.InUse:
                return Response('Already in use')
            if inst.owner is not None:
                return Response('Already in use')
            else:
                setattr(inst, 'owner', request.user)
                setattr(inst, 'InUse', True)
                inst.save()
                return Response('Installation connected', status.HTTP_200_OK)
        except:
            return Response('Wrong primary key', status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def UserUpdate(request):
    cur_count = Installation.objects.filter(owner=request.user)
    if cur_count.count() < 1:
        return Response('You dont have any installations on your account')
    else:
        inst = Installation.objects.get(owner=request.user)
        serializer = InstForCurrentUserSerializer(
            instance=inst, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
