from django.shortcuts import render, redirect, get_object_or_404
from listo.models import Checklist, ChecklistItem
from listo.forms import ChecklistForm, ChecklistItemForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def checklists_list(request):
    checklists = Checklist.objects.all()
    return render(request, "listo/checklists_list.html", {
        "lists": checklists,
    })


def checklists_detail(request, pk):
    checklist = get_object_or_404(Checklist, pk=pk)

    if request.method == "POST":
        checklist_item_form = ChecklistItemForm(request.POST)
        if checklist_item_form.is_valid():
            new_item = checklist_item_form.save(commit=False)
            new_item.checklist = checklist

            last_item = checklist.items.order_by('-order')[0]
            new_item.order = last_item.order + 1

            new_item.save()

            return redirect(to='checklists_detail', pk=pk)
    else:
        checklist_item_form = ChecklistItemForm()

    return render(request, "listo/checklists_detail.html", {
        "item_form": checklist_item_form,
        "checklist": checklist,
    })


def checklists_create(request):
    if request.method == "POST":  # form was submitted
        form = ChecklistForm(request.POST)
        if form.is_valid():
            checklist = form.save()
            return redirect(to=checklist)
    else:
        form = ChecklistForm()

    return render(request, "listo/checklists_create.html", {"form": form})


def checklists_edit(request, pk):
    checklist = get_object_or_404(Checklist, pk=pk)

    if request.method == "POST":
        form = ChecklistForm(instance=checklist, data=request.POST)
        if form.is_valid():
            checklist = form.save()
            return redirect(to=checklist)
    else:
        form = ChecklistForm(instance=checklist)

    return render(request, 'listo/checklists_edit.html', {
        "checklist": checklist,
        "form": form,
    })


def checklists_delete(request, pk):
    checklist = get_object_or_404(Checklist, pk=pk)
    if request.method == "POST":
        checklist.delete()
        return redirect(to='checklists_list')

    return render(request, 'listo/checklists_delete.html',
                  {"checklist": checklist})


def checklist_items_edit(request, pk):
    checklist_item = get_object_or_404(ChecklistItem, pk=pk)
    new_body = request.POST.get('body')
    if new_body:
        checklist_item.body = new_body
        checklist_item.save()
    return redirect(to='checklists_detail', pk=checklist_item.checklist.pk)


@csrf_exempt
def checklists_reorder(request, pk):
    checklist = get_object_or_404(Checklist, pk=pk)

    body = request.body.decode("UTF-8")
    ids = json.loads(body)
    for order, pk in enumerate(ids):
        item = checklist.items.get(pk=int(pk))
        item.order = order
        item.save()

    return JsonResponse({"ok": True})
