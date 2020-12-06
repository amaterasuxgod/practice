from django.urls import path, include
from .views import Create, View, Delete, Update, UserView, UserConnect, UserUpdate


urlpatterns = [
    path('create/', Create, name="create"),
    path('view/', View, name="view"),
    path('delete/<str:pk>/', Delete, name="delete"),
    path('update/<str:pk>/', Update, name="update"),
    path('curinst/', UserView, name="userview"),
    path('connect/<str:pk>/', UserConnect, name="connect"),
    path('userupdate/', UserUpdate, name="user_update"),
]
