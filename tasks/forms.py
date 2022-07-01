from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task #the model we are creating a form for
        fields = '__all__'# to import all fields