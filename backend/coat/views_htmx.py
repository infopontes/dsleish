from django.shortcuts import render
from django.http import HttpResponse
from .models import Coat

def check_coat(request):
    coat = request.GET.get('name')
    coats = Coat.objects.filter(name=coat)
    return render(request, 'partials/htmx/check_name_coat.html', {'coats': coats})