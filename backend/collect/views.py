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

from .models import Collect
from .forms import CollectForm


class CollectListView(HasRoleMixin, LoginRequiredMixin, ListView):
    allowed_roles = ['researcher', 'student']
    model = Collect
    paginate_by = 10


class CollectDetailView(HasRoleMixin, LoginRequiredMixin, DetailView):
    allowed_roles = 'researcher'
    model = Collect


class CollectCreateView(HasRoleMixin, LoginRequiredMixin, CreateView):
    allowed_roles = 'researcher'
    model = Collect
    form_class = CollectForm
    success_url = reverse_lazy('collect:collect_list')
    
    
class CollectUpdateView(HasRoleMixin, LoginRequiredMixin, UpdateView):
    allowed_roles = 'researcher'
    model = Collect
    form_class = CollectForm
    # success_url = reverse_lazy('race:race_list')
    

class CollectDeleteView(HasRoleMixin, DeleteView):
    allowed_roles = 'admin'
    model = Collect
    success_url = reverse_lazy("collect:collect_list")