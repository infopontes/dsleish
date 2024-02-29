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

from .models import Specie
from .forms import SpecieForm


class SpecieListView(LoginRequiredMixin, ListView):
    model = Specie
    paginate_by = 30


class SpecieDetailView(LoginRequiredMixin, DetailView):
    model = Specie


class SpecieCreateView(LoginRequiredMixin, CreateView):
    model = Specie
    form_class = SpecieForm
    success_url = reverse_lazy('specie:specie_list')
    
    
class SpecieUpdateView(LoginRequiredMixin, UpdateView):
    model = Specie
    form_class = SpecieForm
    # success_url = reverse_lazy('race:race_list')
    

def specie_delete(LoginRequiredMixin, request, pk):
    instance = Specie.objects.get(pk=pk)
    instance.delete()
    return redirect('specie:specie_list')