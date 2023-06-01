from django.db import models
from TaskKit.tasks.models.project import Project
from TaskKit.tasks.models.task import Task


class TaskGroup(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)
    description = models.TextField()
    background_image = models.ImageField(upload_to='task_group_backgrounds/', null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='task_groups')
    tasks = models.ManyToManyField(Task, related_name='task_groups')

    def __str__(self):
        return self.name
