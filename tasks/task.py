# from celery import shared_task
from celery import shared_task
from .models import Task



@shared_task
def change_avalability(instance_id):
    instance = Task.objects.get(id=instance_id)
    instance.available = False
    instance.save()
