from django.contrib import admin
from . import views
from django.urls import path, include  # Import the include function

urlpatterns = [
    path('',views.index,name='index'),
    path('task',views.task,name='task')
]