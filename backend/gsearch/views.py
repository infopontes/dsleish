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

from .models import Gsearch
from .forms import GsearchForm


class GsearchListView(LoginRequiredMixin, ListView):
    model = Gsearch
    paginate_by = 30


class GsearchDetailView(LoginRequiredMixin, DetailView):
    model = Gsearch


class GsearchCreateView(LoginRequiredMixin, CreateView):
    model = Gsearch
    form_class = GsearchForm
    success_url = reverse_lazy('gsearch:gsearch_list')
    
    
class GsearchUpdateView(LoginRequiredMixin, UpdateView):
    model = Gsearch
    form_class = GsearchForm
    

class GsearchDeleteView(DeleteView):
    model = Gsearch
    success_url = reverse_lazy("gsearch:gsearch_list")