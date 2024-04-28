from django import forms

from .models import Gsearch

from backend.users.models import User
from backend.project.models import Project

class GsearchForm(forms.ModelForm):
    
    class Meta:
        model = Gsearch
        fields = ('project', 'user', 'name', 'description')
        
        widgets = {
            "project": forms.Select(),
            "user": forms.Select(),
        }
