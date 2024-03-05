from django import forms
from .models import*

class FoodMenuItemsForm(forms.ModelForm):
    
    class Meta:
        model = FoodMenu
        fields = '__all__'
