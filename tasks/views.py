from django.shortcuts import render
from .models import Task
from django.views import View
def view_tasks(request):
    tasks = Task.objects.all()
    return render(request, "view.html",context={'tasks':tasks})

