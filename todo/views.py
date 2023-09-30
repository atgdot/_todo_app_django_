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
    if request.method == 'POST':
        task_id = request.POST.get('task_id')
        completed = request.POST.get('comp', False)  # Default to False if the checkbox is not checked
        print(task_id)
        try:
            post = tasks.objects.get(pk=task_id)
        except tasks.DoesNotExist:
            # Handle the case where the task with the given ID does not exist
            pass
        else:
            post.completed = (completed == 'on')
            post.save()

    post = tasks.objects.all()  # Define 'post' outside of the if block
    return render(request, 'task.html', {'posts': post})  # 'post' is now available in all branches