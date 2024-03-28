from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """ Создание пользваотеля """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        obj = serializer.save()

        # Шифрование пароля
        obj.set_password(serializer.validated_data['password'])
        obj.save()


class UserListAPIView(generics.ListAPIView):
    """ Вывод всех пользователй """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailAPIView(generics.RetrieveAPIView):
    """ Подробный просмотр одного пользователя """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserUpdateAPIView(generics.UpdateAPIView):
    """ Обновление пользователя """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDeleteAPIView(generics.DestroyAPIView):
    """ Удаление пользователя """
    queryset = User.objects.all()
    permission_classes = [AllowAny]
