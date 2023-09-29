from django.db import models

# Create your models here.
class tasks(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title