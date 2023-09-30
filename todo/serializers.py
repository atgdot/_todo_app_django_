from rest_framework import serializers
from .models import tasks

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = tasks
        fields = '__all__'


