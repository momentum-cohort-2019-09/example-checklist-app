from django.db import models


class Checklist(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(
        help_text="Any instructions people need to use this checklist.",
        blank=True,
        null=True)

    def __str__(self):
        return self.title
