from django import forms


class ChecklistForm(forms.Form):
    title = forms.CharField(label="List name", max_length=100)
    description = forms.CharField(widget=forms.Textarea, required=False)
