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

from .models import Breed
from .forms import BreedForm


class BreedListView(LoginRequiredMixin, ListView):
    model = Breed
    paginate_by = 30


class BreedDetailView(LoginRequiredMixin, DetailView):
    model = Breed


class BreedCreateView(LoginRequiredMixin, CreateView):
    model = Breed
    form_class = BreedForm
    success_url = reverse_lazy('breed:breed_list')
    
    
class BreedUpdateView(LoginRequiredMixin, UpdateView):
    model = Breed
    form_class = BreedForm
    # success_url = reverse_lazy('race:race_list')
    

def breed_delete(LoginRequiredMixin, request, pk):
    instance = Breed.objects.get(pk=pk)
    instance.delete()
    return redirect('breed:breed_list')