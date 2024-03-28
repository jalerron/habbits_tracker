from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase
from users.models import User
from habits.models import Habits


class HabitTest(APITestCase):
    def setUp(self):
        """ Создание пользователя в тесте и его авторизация"""
        self.client = APIClient()
        self.user = User.objects.create(
            id=1,
            email="admin@admin.admin",
            password="admin",
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        self.user.set_password("admin")
        self.user.save()
        self.client.force_authenticate(user=self.user)

        self.habit = Habits.objects.create(
            place="Дом",
            time="14:00:00",
            action="Поставить чайник греться",
            periodicity="Sunday",
            reward="Попить чай",
            duration=60,
            is_public=True,
            user=self.user
        )
        self.habit.save()

    def test_create_habit(self):
        """ Создание привычки """
        data = {
            "place": "Дома",
            "time": "11:00:00",
            "action": "заварить чай",
            "periodicity": "Saturday",
            "duration": 120,
            "is_public": True,
            "user": self.user.pk
        }

        response = self.client.post(reverse('habits:create-habit'), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Habits.objects.filter(place=data['place']).exists())

    def test_get_public_habits(self):
        """ Тест получения информации о общедоступных привычках """
        user2 = User.objects.create(
            id=2,
            email="test2@test.test",
            password="test",
            is_superuser=False,
            is_staff=False,
            is_active=True,
        )
        user2.set_password("test")
        user2.save()

        data = {
            "place": "На стадионе",
            "time": "16:00:00",
            "action": "Подтянуться 10 раз",
            "periodicity": "Monday",
            "reward": "Выпить воды",
            "duration": 120,
            "is_public": True,
            "user": user2.pk
        }

        data2 = {
            "place": "На улице",
            "time": "08:00:00",
            "action": "Утренняя зарядка",
            "is_nice": True,
            "periodicity": "Wednesday",
            "duration": 60,
            "is_public": False,
            "user": user2.pk
        }

        self.client.post(reverse('habits:create-habit'), data)
        self.client.post(reverse('habits:create-habit'), data2)
        response = self.client.get(reverse('habits:public-habits'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)

    def test_list_habits(self):
        """ Вывод списка привычек """
        user3 = User.objects.create(
            id=3,
            email="test2@test.test",
            password="test",
            is_superuser=False,
            is_staff=True,
            is_active=True
        )
        user3.set_password("test")
        user3.save()

        data = {
            "place": "На стадионе",
            "time": "16:00:00",
            "action": "Подтянуться 10 раз",
            "periodicity": "Monday",
            "reward": "Выпить воды",
            "duration": 120,
            "is_public": True,
            "user": user3.pk
        }

        data2 = {
            "place": "На улице",
            "time": "08:00:00",
            "action": "Утренняя зарядка",
            "is_nice": True,
            "periodicity": "Wednesday",
            "duration": 60,
            "is_public": False,
            "user": user3.pk
        }

        self.client.post(reverse('habits:create-habit'), data=data)
        self.client.post(reverse('habits:create-habit'), data=data2)
        response = self.client.get(reverse('habits:list-habit'), )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 3)

    def test_detail_habits(self):
        """ Тест детального просмотра привычки """

        habit_pk = Habits.objects.first().pk

        response = self.client.get(reverse('habits:detail-habit', args=[habit_pk]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_habits(self):
        """ Тест обновления привычки """
        data = {
            "place": "Дома",
            "time": "11:00:00",
            "action": "заварить чай",
            "periodicity": "Saturday",
            "duration": 120,
            "is_public": True,
            "user": self.user.pk
        }

        data2 = {
            "place": "home"
        }

        self.client.post('habits:create-habit', data)
        habit_pk = Habits.objects.first().pk
        response = self.client.put(reverse('habits:update-habit', args=[habit_pk]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_habit(self):

        delete_url = reverse('habits:delete-habit', args=[self.habit.id])
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
