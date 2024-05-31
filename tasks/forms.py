from django import forms
from .models import Tasks

class CreateTaskForm(forms.Form):
    class Meta:
        model = Tasks
        fields = ['title_task','description_task']