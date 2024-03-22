from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

from users.views import UserCreateAPIView, UserListAPIView, UserDetailAPIView, UserUpdateAPIView, UserDeleteAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('create/', UserCreateAPIView.as_view(), name='create-user'),
    path('list/', UserListAPIView.as_view(), name='list-users'),
    path('detail/<int:pk>/', UserDetailAPIView.as_view(), name='detail-user'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update-user'),
    path('delete/<int:pk>/', UserDeleteAPIView.as_view(), name='delete-user'),

    path('token/', TokenObtainPairView.as_view(), name='token-obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
