from datetime import datetime

from celery import shared_task

from habits.models import Habits
from habits.services import send_message

weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")


@shared_task
def habits_scheduler():
    current_time = datetime.now().replace(second=0, microsecond=0)  # Настоящее время без секунд и микросекунд
    current_day = weekDays[datetime.today().weekday()]
    try:
        # привычкеа по фильтру: не приятная, и id чат телеграмма не пустое
        habits = Habits.objects.filter(is_nice=False, periodicity__in=[current_day, 'DAILY'],
                                       user__chat_id__isnull=False)
        for habit in habits:
            if habit.time.strftime('%H:%M:%S') == current_time.strftime('%H:%M:%S'):
                id_chat = habit.user.chat_id
                message = f'Вам необходимо выполнить привычку: {habit.action} \n'
                if habit.reward:
                    message += f'Вознаграждение: {habit.reward} \n'

                elif habit.related_habits:
                    message += f'У вас есть связанная привычка: {habit.related_habits.action} \n'

                else:
                    message += f'Вознаграждения и связанной привычки нет.'

                send_message(chat_id=id_chat, text=message)
    except Exception as e:
        print(f'Error: {e}')
