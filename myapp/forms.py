from .models import employee
from django import forms

class employeeform(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'
