from django.db import models
from django.contrib.auth.models import User


class Community(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='communities')
    color = models.CharField(max_length=8)
    is_open = models.BooleanField(default=0)
    is_public = models.BooleanField(default=0)
    creation_date = models.DateTimeField(auto_now_add=True)
    founder_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='founded_communities')

    @property
    def number_of_members(self):
        return self.members.count()
    @property
    def number_of_projects(self):
        return self.projects.all().count()
    @property
    def number_of_tasks(self):
        return self.projects.values_list('tasks', flat=1).count()

    def __str__(self):
        return self.name
