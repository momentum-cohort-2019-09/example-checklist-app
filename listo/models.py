from django.db import models


class Checklist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(
        help_text="Any instructions people need to use this checklist.",
        blank=True,
        null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ChecklistItem(models.Model):
    body = models.CharField(max_length=255)
    checklist = models.ForeignKey(to=Checklist,
                                  on_delete=models.CASCADE,
                                  related_name='items')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body