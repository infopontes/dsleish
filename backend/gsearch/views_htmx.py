from django.shortcuts import render
from django.http import HttpResponse
from .models import Animal

def check_animal(request):
    animal = request.GET.get('name')
    animals = Animal.objects.filter(name=animal)
    return render(request, 'partials/htmx/check_name_animal.html', {'animals': animals})