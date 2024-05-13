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

from .models import Coat
from .forms import CoatForm


class CoatListView(HasRoleMixin, LoginRequiredMixin, ListView):
    allowed_roles = ['researcher', 'student']
    model = Coat
    paginate_by = 30


class CoatDetailView(HasRoleMixin, LoginRequiredMixin, DetailView):
    allowed_roles = 'researcher'
    model = Coat


class CoatCreateView(HasRoleMixin, LoginRequiredMixin, CreateView):
    allowed_roles = 'researcher'
    model = Coat
    form_class = CoatForm
    success_url = reverse_lazy('coat:coat_list')
    
    
class CoatUpdateView(HasRoleMixin, LoginRequiredMixin, UpdateView):
    allowed_roles = 'researcher'
    model = Coat
    form_class = CoatForm
    # success_url = reverse_lazy('race:race_list')
    
class CoatDeleteView(HasRoleMixin, DeleteView):
    allowed_roles = 'admin'
    model = Coat
    success_url = reverse_lazy("coat:coat_list")