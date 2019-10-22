from django.contrib import admin

from listo.models import Checklist, ChecklistItem


class ChecklistItemInline(admin.TabularInline):
    model = ChecklistItem
    extra = 3


class ChecklistAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'item_count',
        'updated_at',
    )

    inlines = [ChecklistItemInline]


admin.site.register(Checklist, ChecklistAdmin)
admin.site.register(ChecklistItem)
