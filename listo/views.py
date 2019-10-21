from django.shortcuts import render
from listo.data import CHECKLISTS


# Create your views here.
def checklists_list(request):
    return render(request, "listo/checklists_list.html", {
        "lists": CHECKLISTS,
    })
