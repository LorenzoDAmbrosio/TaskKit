from django.db import models
from django import forms

from TaskKit.tasks.models.community import Community

class Project(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)
    community = models.ForeignKey(Community, on_delete=models.CASCADE, related_name='projects')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
