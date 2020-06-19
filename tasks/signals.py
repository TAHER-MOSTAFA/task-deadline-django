from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Task
from .task import change_avalability


@receiver(post_save, sender=Task)
def task_availabilty(sender, instance, *args, **kwargs):
    change_avalability.apply_async((instance.id,),countdown=instance.time.total_seconds())