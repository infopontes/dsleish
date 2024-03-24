from django import forms

from .models import Breed

class BreedForm(forms.ModelForm):
    
    class Meta:
        model = Breed
        fields = ('name', 'description', 'specie')
        
        widgets = {
            "specie": forms.Select()
        }