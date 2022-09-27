from dataclasses import field
from pyexpat import model
from tabnanny import check
from django import forms
from todolist.models import Task

class CreateNewTask(forms.ModelForm):
    # title = forms.CharField(label="Judul", max_length=200)
    # check = forms.BooleanField(required=False)
    # date = forms.DateField()
    # description = forms.CharField(max_length=1000)
    class Meta:
        model = Task
        fields = ['title', 'description']