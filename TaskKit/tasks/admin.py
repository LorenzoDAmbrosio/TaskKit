from django.contrib import admin
from .models import *

admin.site.register(Task)
admin.site.register(TaskGroup)
admin.site.register(Community)
admin.site.register(Status)
admin.site.register(Project)