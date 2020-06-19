from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    time = models.DurationField(default='0:0:0')
    available = models.BooleanField(default=True)