from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tasks(models.Model):
    title_task = models.CharField(max_length=100)
    description_task = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.description_task