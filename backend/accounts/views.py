from django.shortcuts import render
#from django.contrib.auth.forms import UserCreationForm
from backend.users.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from django.views import generic

    
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
    
class ChangeUser(generic.UpdateView):
    form_class = UserChangeForm
    success_url = reverse_lazy('login')
    template_name = 'registration/change.html'