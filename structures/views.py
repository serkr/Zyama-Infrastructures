from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django import forms


from .forms import StructureForm
from .models import Category, Structure


def index(request):
    cat = Category.objects.all()
    return render(request, 'structures/index.html', {'cat' : cat})
    
def stru(request, cat_id):
    stru = (Category.objects.get(pk=cat_id)).structure_set.all()
    return render(request, 'structures/gyms.html', {'stru' : stru})

def add_edit_struc(request, n_id = None):
    #import ipdb; ipdb.set_trace()
    if request.method == "POST":
        if n_id:
            n = Structure.objects.get(id=n_id)
            form = StructureForm(request.POST, instance = n)
            form.save()
            #import ipdb; ipdb.set_trace()
            cat_id_new = Structure.objects.get(pk = n_id).category.id
            return redirect('stru', cat_id_new)
        form = StructureForm(request.POST)
        form.save()
        return redirect('stru', form.data['category'])
    elif n_id:
        fields_dict = model_to_dict(Structure.objects.get(id=n_id))
        form = StructureForm(fields_dict)
        return render(request, 'structures/edit.html', {'form': form})
    else:
        form = StructureForm()
        return render(request, 'structures/edit.html', {'form': form})

