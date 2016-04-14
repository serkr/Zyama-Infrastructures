from django import forms
from .models import Structure

class StructureForm(forms.ModelForm):

    class Meta:
        model = Structure
        fields = ('name', 'adress', 'work_status', 'comment', 'category')