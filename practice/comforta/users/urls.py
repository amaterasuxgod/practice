from django.urls import path, include
from .views import Register, Login, AllUsersView, DeleteUserView


urlpatterns = [
    path('register/', Register, name="register"),
    path('login/', Login, name="login"),
    path('all/', AllUsersView, name="all"),
    path('delete/<str:pk>/', DeleteUserView, name="delete-user")
]
