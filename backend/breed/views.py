from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)

from .models import Breed
from .forms import BreedForm

class BreedListView(ListView):
    model = Breed
    paginate_by = 30


class BreedDetailView(DetailView):
    model = Breed


class BreedCreateView(CreateView):
    model = Breed
    form_class = BreedForm
    success_url = reverse_lazy('breed:breed_list')
    
    
class BreedUpdateView(UpdateView):
    model = Breed
    form_class = BreedForm
    # success_url = reverse_lazy('race:race_list')
    

def breed_delete(request, pk):
    instance = Breed.objects.get(pk=pk)
    instance.delete()
    return redirect('breed:breed_list')