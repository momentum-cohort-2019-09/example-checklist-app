from django.shortcuts import render
from listo.models import Checklist


# Create your views here.
def checklists_list(request):
    checklists = Checklist.objects.all()
    return render(request, "listo/checklists_list.html", {
        "lists": checklists,
    })


def checklists_detail(request, pk):
    checklist = Checklist.objects.get(pk=pk)
    return render(request, "listo/checklists_detail.html",
                  {"checklist": checklist})
