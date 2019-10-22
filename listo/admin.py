from django.contrib import admin

from listo.models import Checklist, ChecklistItem

admin.site.register(Checklist)
admin.site.register(ChecklistItem)
