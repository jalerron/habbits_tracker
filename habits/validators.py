class HabitValidatorRelatedNice:

    def __init__(self, field_nice, field_reward):
        self.field_nice = field_nice
        self.field_reward = field_reward

    def __call__(self, value):
        is_nice = value.get(self.field_nice)
        field_reward = value.get(self.field_reward)

        if is_nice and field_reward:
            raise ValueError('Должно быть заполнено только одно поле (связаная привычка или признак приятной привычки)')


class HabitValidatorTimeForWork:

    def __init__(self, field):
        self.filed = field

    def __call__(self, value):
        time_to_work = value.get(self.filed)

        if time_to_work > 120:
            raise ValueError('Время выполнения может быть не более 120 секунд')


class HabitValidatorRelated:

    def __init__(self, field_nice, field_related):
        self.field_nice = field_nice
        self.field_related = field_related

    def __call__(self, value):
        is_nice = value.get(self.field_nice)
        is_related = value.get(self.field_related)

        if is_related and not is_related.is_nice:
            raise ValueError('В связанные привычки можно добавлять только с признаком приятной')


class HabitValidatorNiceReward:

    def __init__(self, field_nice, field_related):
        self.field_nice = field_nice
        self.field_related = field_related

    def __call__(self, value):
        is_nice = value.get(self.field_nice)
        is_related = value.get(self.field_related)

        if is_nice and is_related:
            raise ValueError('У приятной привычки не может быть вознаграждения или связанной привычки')


class HabitsValidatorRule:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        field_periodicity = value.get(self.field)

        if field_periodicity > 7:
            raise ValueError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')
