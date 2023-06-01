from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from django import forms

from TaskKit.tasks.models.project import Project


class Task(models.Model):
    title = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks_assigned', null=True,
                                    blank=True)
    color = models.CharField(max_length=8, blank=True, default='000000FF')
    description = models.TextField(blank=True)
    background_image = models.ImageField(upload_to='task_backgrounds/', null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True, blank=True, related_name='tasks')
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def clean(self):
        super().clean()
        if self.status and self.project and self.status not in self.project.statuses.all():
            raise ValidationError("Invalid status assignment for this task's project.")
        if self.assigned_to and self.project and self.assigned_to not in self.project.community.members.all():
            raise ValidationError("Invalid assigned user for this task's project.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
