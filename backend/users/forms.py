from django.contrib.auth import forms

from .models import User


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
        
class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
        
class PasswordChangingForm(forms.PasswordChangeForm):
    class Meta(forms.PasswordChangeForm):
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']