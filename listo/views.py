from django.shortcuts import render, redirect
from listo.models import Checklist
from listo.forms import ChecklistForm


# Create your views here.
def checklists_list(request):
    checklists = Checklist.objects.all()
    return render(request, "listo/checklists_list.html", {
        "lists": checklists,
    })


def checklists_detail(request, pk):
    checklist = Checklist.objects.get(pk=pk)
    items = checklist.items
    return render(request, "listo/checklists_detail.html", {
        "checklist": checklist,
        "items": items,
    })


def checklists_create(request):
    if request.method == "POST":  # form was submitted
        form = ChecklistForm(request.POST)
        if form.is_valid():
            checklist = Checklist()
            checklist.title = form.cleaned_data['title']
            checklist.description = form.cleaned_data['description']
            # OR checklist = Checklist(**form.cleaned_data)

            checklist.save()
            return redirect(to='checklists_list')
    else:
        form = ChecklistForm()

    return render(request, "listo/checklists_create.html", {"form": form})
