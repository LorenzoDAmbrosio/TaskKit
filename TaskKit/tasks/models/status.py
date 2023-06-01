from django.db import models

from TaskKit.tasks.models import Project


class Status(models.Model):
    label = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='statuses')

    def __str__(self):
        return self.label