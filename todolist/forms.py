from tabnanny import check
from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Judul", max_length=200)
    check = forms.BooleanField(required=False)
    date = forms.DateField()
    description = forms.TimeField()