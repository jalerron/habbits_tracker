# Generated by Django 5.0.2 on 2024-03-25 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0003_alter_habits_periodicity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='duration',
            field=models.PositiveIntegerField(default=60, verbose_name='время выполнения'),
        ),
    ]
