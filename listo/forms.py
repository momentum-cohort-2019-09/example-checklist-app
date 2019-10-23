from django import forms
from listo.models import Checklist


class ChecklistForm(forms.ModelForm):

    class Meta:
        model = Checklist
        fields = ['title', 'description']
