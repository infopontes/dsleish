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

from .models import Breed
from .forms import BreedForm


class BreedListView(HasRoleMixin, LoginRequiredMixin, ListView):
    allowed_roles = ['researcher', 'student']
    model = Breed
    paginate_by = 30


class BreedDetailView(HasRoleMixin, LoginRequiredMixin, DetailView):
    allowed_roles = 'researcher'
    model = Breed


class BreedCreateView(HasRoleMixin, LoginRequiredMixin, CreateView):
    allowed_roles = 'researcher'
    model = Breed
    form_class = BreedForm
    success_url = reverse_lazy('breed:breed_list')
    
    
class BreedUpdateView(HasRoleMixin, LoginRequiredMixin, UpdateView):
    allowed_roles = 'researcher'
    model = Breed
    form_class = BreedForm
    # success_url = reverse_lazy('race:race_list')
    

class BreedDeleteView(HasRoleMixin, DeleteView):
    allowed_roles = 'admin'
    model = Breed
    success_url = reverse_lazy("breed:breed_list")