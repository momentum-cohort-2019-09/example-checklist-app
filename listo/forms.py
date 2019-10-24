from django import forms
from listo.models import Checklist, ChecklistItem


class ChecklistForm(forms.ModelForm):

    class Meta:
        model = Checklist
        fields = ['title', 'description']


class ChecklistItemForm(forms.ModelForm):

    class Meta:
        model = ChecklistItem
        fields = ['body']
