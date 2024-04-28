from django.shortcuts import render, redirect
from django.urls import reverse_lazy
# from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from .models import Project
from .forms import ProjectForm


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    paginate_by = 30


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('project:project_list')
    
    
class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    # success_url = reverse_lazy('race:race_list')
    

class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy("project:project_list")