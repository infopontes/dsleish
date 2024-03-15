from django import forms

from .models import Coat

class CoatForm(forms.ModelForm):
    
    class Meta:
        model = Coat
        fields = ('name', 'description',)