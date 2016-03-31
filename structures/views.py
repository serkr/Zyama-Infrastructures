from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import StructureForm
from .models import Category, Structure


def index(request):
    cat = Category.objects.all()
    return render(request, 'structures/index.html', {'cat' : cat})
    
def stru(request, cat_id):
    stru = (Category.objects.get(pk=cat_id)).structure_set.all()
    return render(request, 'structures/gyms.html', {'stru' : stru})

def add_edit_struc(request):
    if request.method == "POST":
        form = StructureForm(request.POST)
        if form.is_valid():
            structure.save()
    else:
        form = StructureForm()
    return render(request, 'structures/edit.html', {'form': form})

