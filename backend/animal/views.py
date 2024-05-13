from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from rolepermissions.mixins import HasRoleMixin


from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from .models import Animal
from .forms import AnimalForm


class AnimalListView(HasRoleMixin, LoginRequiredMixin, ListView):
    allowed_roles = ['researcher', 'student']
    model = Animal
    paginate_by = 30


class AnimalDetailView(HasRoleMixin, LoginRequiredMixin, DetailView):
    allowed_roles = 'researcher'
    model = Animal


class AnimalCreateView(HasRoleMixin, LoginRequiredMixin, CreateView):
    allowed_roles = 'researcher'
    model = Animal
    form_class = AnimalForm
    success_url = reverse_lazy('animal:animal_list')
    
    
class AnimalUpdateView(HasRoleMixin, LoginRequiredMixin, UpdateView):
    allowed_roles = 'researcher'
    model = Animal
    form_class = AnimalForm
    # success_url = reverse_lazy('race:race_list')
    

class AnimalDeleteView(HasRoleMixin, DeleteView):
    allowed_roles = 'admin'
    model = Animal
    success_url = reverse_lazy("animal:animal_list")