from django.urls import path, include
from .views import Create, View, Delete


urlpatterns = [
    path('create/', Create, name="create"),
    path('view/<str:pk>/', View, name="view"),
    path('delete/<str:pk>/', Delete, name="delete")
]
