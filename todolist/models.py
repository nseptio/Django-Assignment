from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class ToDoList(models.Model):
#     user = models.ForeignKey(User, on_delete=CASCADE)
#     name = models.CharField(max_length=100)

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add= True)
    title = models.CharField(max_length= 200)
    description = models.TextField()
    is_finished = models.BooleanField(default= False)
    
    def __str__(self):
        return self.title

    