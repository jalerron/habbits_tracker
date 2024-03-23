from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from habits.models import Habits
from habits.serializers import HabitSerializer


class HabitsListAPIView(generics.ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]


class HabitsCreateAPIView(generics.CreateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]


class HabitsUpdateAPIView(generics.UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]


class HabitsDetailAPIView(generics.RetrieveAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [AllowAny]


class HabitsDeleteAPIView(generics.DestroyAPIView):
    queryset = Habits.objects.all()
    permission_classes = [AllowAny]