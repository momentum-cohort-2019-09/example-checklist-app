from django.db import models
from django.urls import reverse


class Checklist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(
        help_text="Any instructions people need to use this checklist.",
        blank=True,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def item_count(self):
        return self.items.count()

    def get_absolute_url(self):
        return reverse("checklists_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title


class ChecklistItem(models.Model):

    class Meta:
        ordering = ['order']

    body = models.CharField(max_length=255)
    checklist = models.ForeignKey(to=Checklist,
                                  on_delete=models.CASCADE,
                                  related_name='items')
    order = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body
