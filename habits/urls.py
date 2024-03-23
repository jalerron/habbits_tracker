from django.urls import path

from habits.apps import HabbitsConfig
from habits.views import HabitsListAPIView, HabitsCreateAPIView, HabitsDetailAPIView, HabitsUpdateAPIView, \
    HabitsDeleteAPIView

app_name = HabbitsConfig.name

urlpatterns = [
    path('list/', HabitsListAPIView.as_view(), name='list-habit'),
    path('create/', HabitsCreateAPIView.as_view(), name='create-habit'),
    path('detail/<int:pk>/', HabitsDetailAPIView.as_view(), name='detail-habit'),
    path('update/<int:pk>/', HabitsUpdateAPIView.as_view(), name='update-habit'),
    path('delete/<int:pk>/', HabitsDeleteAPIView.as_view(), name='delete-habit'),
]
