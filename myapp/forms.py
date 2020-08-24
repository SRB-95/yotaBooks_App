from django import forms
from .models import Person

class ItemForm(forms.ModelForm):
    class Meta:
        model=Person							
        fields = ['first_name','last_name','contact','email','user_name','image']
