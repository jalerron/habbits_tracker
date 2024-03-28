from rest_framework import serializers

from habits.models import Habits
from habits.validators import HabitValidatorRelatedNice, HabitValidatorTimeForWork, HabitValidatorRelated, \
    HabitValidatorNiceReward, HabitsValidatorRule


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        validators = [
            HabitValidatorRelatedNice(field_nice='is_nice', field_reward='reward'),
            HabitValidatorTimeForWork(field='duration'),
            HabitValidatorRelated(field_nice='is_nice', field_related='related_habits'),
            HabitValidatorNiceReward(field_nice='is_nice', field_related='related_habits'),
            # HabitsValidatorRule(field='periodicity')
        ]
        fields = '__all__'