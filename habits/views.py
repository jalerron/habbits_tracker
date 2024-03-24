from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

from habits.models import Habits
from habits.pagination import HabitPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer


class HabitsListAPIView(generics.ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]
    pagination_class = HabitPagination


class HabitsCreateAPIView(generics.CreateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.user = self.request.user
        habit.save()


class HabitsUpdateAPIView(generics.UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsDetailAPIView(generics.RetrieveAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner | IsAdminUser]


class HabitsDeleteAPIView(generics.DestroyAPIView):
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class PublicHabitListApiView(generics.ListAPIView):
    queryset = Habits.objects.filter(is_public=True)
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination
