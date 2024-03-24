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

from .models import Animal
from .forms import AnimalForm


class AnimalListView(LoginRequiredMixin, ListView):
    model = Animal
    paginate_by = 30


class AnimalDetailView(LoginRequiredMixin, DetailView):
    model = Animal


class AnimalCreateView(LoginRequiredMixin, CreateView):
    model = Animal
    form_class = AnimalForm
    success_url = reverse_lazy('animal:animal_list')
    
    
class AnimalUpdateView(LoginRequiredMixin, UpdateView):
    model = Animal
    form_class = AnimalForm
    # success_url = reverse_lazy('race:race_list')
    

class AnimalDeleteView(DeleteView):
    model = Animal
    success_url = reverse_lazy("animal:animal_list")