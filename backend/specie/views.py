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

from .models import Specie
from .forms import SpecieForm


class SpecieListView(HasRoleMixin, LoginRequiredMixin, ListView):
    allowed_roles = ['researcher', 'student']
    model = Specie
    paginate_by = 30


class SpecieDetailView(HasRoleMixin, LoginRequiredMixin, DetailView):
    allowed_roles = 'researcher'
    model = Specie


class SpecieCreateView(HasRoleMixin, LoginRequiredMixin, CreateView):
    allowed_roles = 'researcher'
    model = Specie
    form_class = SpecieForm
    success_url = reverse_lazy('specie:specie_list')
    
    
class SpecieUpdateView(HasRoleMixin, LoginRequiredMixin, UpdateView):
    allowed_roles = 'researcher'
    model = Specie
    form_class = SpecieForm
    # success_url = reverse_lazy('race:race_list')
    
class SpecieDeleteView(HasRoleMixin, DeleteView):
    allowed_roles = 'admin'
    model = Specie
    success_url = reverse_lazy("specie:specie_list")