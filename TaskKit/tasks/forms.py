from django import forms

from TaskKit.tasks.models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'