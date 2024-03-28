from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):

    email = models.EmailField(unique=True, verbose_name='почта')
    full_name = models.CharField(max_length=150, verbose_name='полное имя',
                                 **NULLABLE)
    chat_id = models.CharField(max_length=150, verbose_name='id чат телеграма')

    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def ___str___(self):
        return f'{self.email} - {self.full_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
