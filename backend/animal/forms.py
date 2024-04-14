from django import forms

from .models import Animal

class AnimalForm(forms.ModelForm):
    
    class Meta:
        model = Animal
        fields = ('name', 'owner', 'phone_number', 'id_db_original', 'name_chip', 'breed', 'coat', 'sex', 'caracteristics')
        
        widgets = {
            "breed": forms.Select(),
            "coat": forms.Select(),
            "sex": forms.Select(),
        }
    
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['phone_number'].widget.attrs.update({'class': 'mask-phone'})
        