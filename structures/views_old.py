from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Category, Structure


def index(request):
    cat = Category.objects.all()
    return render(request, 'structures/index.html', {'cat' : cat})
    
def gyms(request):
    g = Structure.objects.all()
    return render(request, 'structures/gyms.html', {'g' : g})
