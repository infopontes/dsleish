from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib.auth.views import PasswordChangeView


from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from .models import User
from .forms import UserChangeForm, PasswordChangingForm


class UserListView(ListView):
    model = User
    

class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    success_url = reverse_lazy('core:index')
    success_message = 'User changed successfully!!!'

# https://youtu.be/P6QHswl2PqE
class PasswordsChangeView(SuccessMessageMixin, PasswordChangeView):
    model = User
    form_class = PasswordChangingForm
    #success_url = reverse_lazy('users:password_success')
    success_url = reverse_lazy('core:index')
    success_message = 'User password changed successfully!!!'
