from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CreateLogSerializer, ViewLogSerializer
from .models import Log
from inst.models import Installation
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from users.models import User
import json
from rest_framework.pagination import PageNumberPagination

# Create your views here.


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Create(request):
    serializer = CreateLogSerializer(data=request.data)
    serializer.is_valid()
    inst = Installation.objects.get(owner=request.user)
    try:
        if inst.id == serializer.data['Installation']:
            serializer1 = CreateLogSerializer(data=request.data)
            if serializer1.is_valid(raise_exception=True):
                serializer1.save()
                return Response(serializer1.data, status=status.HTTP_200_OK)
            return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)
        return Response('This is not your facility', status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except:
        return Response('Bad request', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def View(request, pk):
    if request.user.IsAdmin:
        paginator = PageNumberPagination()
        paginator.page_size = 10
        logs = Log.objects.filter(Installation=pk)
        result_page = paginator.paginate_queryset(logs, request)
        serializer = ViewLogSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    else:
        try:
            inst = Installation.objects.get(id=pk)
            if request.user == inst.owner:
                paginator = PageNumberPagination()
                paginator.page_size = 10
                logs = Log.objects.filter(Installation=pk)
                result_page = paginator.paginate_queryset(logs, request)
                serializer = ViewLogSerializer(result_page, many=True)
                return paginator.get_paginated_response(serializer.data)
            return Response('This installation is not on your account', status.HTTP_400_BAD_REQUEST)
        except:
            return Response('Wrong primary key', status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def Delete(request, pk):
    if request.user.IsAdmin:
        try:
            rm_logs = Log.objects.filter(Installation=pk)
            rm_logs.delete()
            return Response({'detail': 'Logs were deleted'}, status=status.HTTP_200_OK)
        except:
            return Response('Wrong primary key', status=status.HTTP_400_BAD_REQUEST)
    return Response('You must have admin rights to access to this page', status=status.HTTP_405_METHOD_NOT_ALLOWED)
