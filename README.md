# Habit Tracker

WEB приложения трекер привычек


## Запуск проекта

   1. В данном приложении используется виртуальное окружение venv. Для установки зависимосстей выполнить команду: pip install -r requierements.txt
   
   2. Необходимо содать файл .env с параметрами программы, за основу можно взять файл .env_example

   3. Примените миграции:
      * python manage.py migrate - Windows
      * python3 manage.py migrate - Linux

   4. Запустите сервер:
      * python manage.py runserver -Windows
      * python3 manage.py runserver - Linux

   5. Запустите Celery для обработки отложенных задач:
      * celery -A config worker --pool=solo -l INFO
      * celery -A config beat -l info -S django

   6. Подготовьте телеграм бота для отправки данных
      * Запустите бота командой /start
     
## Для создания администратора необходимо выполнить команду:

  * python manage.py csu - Windows
  * python3 manage.py csu - Linux

## Документация API

Документация API доступна после запуска сервера по адресу: http://localhost:8000/redoc/ или http://localhost:8000/swagger/
