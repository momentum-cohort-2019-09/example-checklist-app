from django.shortcuts import render
from listo.data import CHECKLISTS


# Create your views here.
def checklists_list(request):
    return render(request, "listo/checklists_list.html", {
        "lists": CHECKLISTS,
    })


def checklists_detail(request, id):
    checklist = CHECKLISTS[id]
    return render(request, "listo/checklists_detail.html",
                  {"checklist": checklist})
