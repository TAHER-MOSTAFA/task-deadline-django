# Generated by Django 3.0.5 on 2020-06-18 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.DurationField(default='0:0:0'),
        ),
    ]
