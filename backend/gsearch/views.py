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

from .models import Gsearch
from .forms import GsearchForm


class GsearchListView(HasRoleMixin, LoginRequiredMixin, ListView):
    allowed_roles = ['researcher', 'student']
    model = Gsearch
    paginate_by = 30


class GsearchDetailView(HasRoleMixin, LoginRequiredMixin, DetailView):
    allowed_roles = 'researcher'
    model = Gsearch


class GsearchCreateView(HasRoleMixin, LoginRequiredMixin, CreateView):
    allowed_roles = 'researcher'
    model = Gsearch
    form_class = GsearchForm
    success_url = reverse_lazy('gsearch:gsearch_list')
    
    
class GsearchUpdateView(HasRoleMixin, LoginRequiredMixin, UpdateView):
    allowed_roles = 'researcher'
    model = Gsearch
    form_class = GsearchForm
    

class GsearchDeleteView(HasRoleMixin, DeleteView):
    allowed_roles = 'admin'
    model = Gsearch
    success_url = reverse_lazy("gsearch:gsearch_list")