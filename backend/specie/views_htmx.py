from django.shortcuts import render
from django.http import HttpResponse
from .models import Specie

def check_specie(request):
    specie = request.GET.get('name')
    species = Specie.objects.filter(name=specie)
    return render(request, 'partials/htmx/check_name_specie.html', {'species': species})