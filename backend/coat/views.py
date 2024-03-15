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

from .models import Coat
from .forms import CoatForm


class CoatListView(LoginRequiredMixin, ListView):
    model = Coat
    paginate_by = 30


class CoatDetailView(LoginRequiredMixin, DetailView):
    model = Coat


class CoatCreateView(LoginRequiredMixin, CreateView):
    model = Coat
    form_class = CoatForm
    success_url = reverse_lazy('coat:coat_list')
    
    
class CoatUpdateView(LoginRequiredMixin, UpdateView):
    model = Coat
    form_class = CoatForm
    # success_url = reverse_lazy('race:race_list')
    
class CoatDeleteView(DeleteView):
    model = Coat
    success_url = reverse_lazy("coat:coat_list")