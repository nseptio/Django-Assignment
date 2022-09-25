from django.db import models

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey('self', on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    
# class User(models.Model):
    