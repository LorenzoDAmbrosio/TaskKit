from django import forms
from django.contrib.auth.models import User

from TaskKit.tasks.models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = '__all__'
class AccountEditForm:
    class Meta:
        model = User
        fields = '__all__'

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
class CommunityForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = '__all__'