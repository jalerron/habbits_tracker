from django.db import models

from config import settings
from users.models import User

NULLABLE = {"blank": True, "null": True}


class Habits(models.Model):
    class HabitChoices(models.TextChoices):
        Daily = 'DAILY'
        monday = 'Monday'
        tuesday = 'Tuesday'
        wednesday = 'Wednesday'
        thursday = 'Thursday'
        friday = 'Friday'
        saturday = 'Saturday'
        sunday = 'Sunday'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='пользователь', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name="место", **NULLABLE)
    time = models.TimeField(default='12:00:00', verbose_name='время выполнения')
    action = models.CharField(max_length=150, verbose_name="действие")
    is_nice = models.BooleanField(default=False, verbose_name="признак приятности")
    related_habits = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name="привычка", **NULLABLE)
    periodicity = models.CharField(choices=HabitChoices.choices, default=HabitChoices.Daily,
                                   verbose_name='периодичность')  # периодичность
    reward = models.CharField(max_length=150, verbose_name="вознаграждение", **NULLABLE)
    duration = models.PositiveIntegerField(default=60, verbose_name="время выполнения")  # хранит кол-во секунд на выполнение
    is_public = models.BooleanField(default=False, verbose_name="признак публичности")

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
