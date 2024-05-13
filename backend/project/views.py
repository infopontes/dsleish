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

from .models import Project
from .forms import ProjectForm


class ProjectListView(HasRoleMixin, LoginRequiredMixin, ListView):
    allowed_roles = ['researcher', 'student']
    model = Project
    paginate_by = 30


class ProjectDetailView(HasRoleMixin, LoginRequiredMixin, DetailView):
    allowed_roles = 'researcher'
    model = Project


class ProjectCreateView(HasRoleMixin, LoginRequiredMixin, CreateView):
    allowed_roles = 'researcher'
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project:project_list')
    
    
class ProjectUpdateView(HasRoleMixin,LoginRequiredMixin, UpdateView):
    allowed_roles = 'researcher'
    model = Project
    form_class = ProjectForm
    # success_url = reverse_lazy('race:race_list')
    

class ProjectDeleteView(HasRoleMixin,DeleteView):
    allowed_roles = 'admin'
    model = Project
    success_url = reverse_lazy("project:project_list")