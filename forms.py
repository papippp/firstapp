from django import forms
from . import models

class ApplicationForm(forms.ModelForm):
    class Meta():
        model = models.Application
        fields = '__all__'