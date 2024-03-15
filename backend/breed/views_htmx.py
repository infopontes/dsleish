from django.shortcuts import render
from django.http import HttpResponse
from .models import Breed

def check_breed(request):
    breed = request.GET.get('name')
    breeds = Breed.objects.filter(name=breed)
    return render(request, 'partials/htmx/check_name_breed.html', {'breeds': breeds})