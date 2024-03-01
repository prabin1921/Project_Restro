from django.forms import ModelForm
from django import forms
from .models import*


class MenuForm(forms.ModelForm):
    class Meta:
        model = FoodMenu
        fields= '__all__'
        