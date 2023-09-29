from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import tasks
from .serializers import TaskSerializers

def index(request):
    if request.method == 'POST':
        task_title = request.POST.get('taskTitle')
        task_description=request.POST.get('taskDesc')
        print(task_description,task_title)
        dbData = tasks(title=task_title, description=task_description)
        dbData.save()

    return render(request,'index.html')

def task(request):
    post=tasks.objects.all()
    return render(request,'task.html',{'posts':post})