from django import forms

from .models import Animal

class AnimalForm(forms.ModelForm):
    
    class Meta:
        model = Animal
        fields = ('name', 'id_db_original', 'name_chip', 'breed', 'coat', 'sex')
        
        widgets = {
            "breed": forms.Select(),
            "coat": forms.Select(),
            "sex": forms.Select(),
        }