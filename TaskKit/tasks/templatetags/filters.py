import random

from django import template

register = template.Library()

@register.filter
def is_member_of(user, community):
    return user in community.members.all()

@register.filter
def filter_tasks_by_status(tasks,status):
    return tasks.filter(status=status).all()
@register.filter
def count_tasks_by_status(tasks,status):
    return tasks.filter(status=status).all().count()
@register.filter
def percentage_tasks_by_status(tasks,status):
    taskCount=tasks.count()
    statusCount=tasks.filter(status=status).all().count()
    if taskCount is 0 :
        return 0
    return round((statusCount/taskCount)*100.0, 2)

@register.filter
def random_border_color(string):
    colors = [
        "border-primary",
        "border-success",
        "border-danger",
        "border-warning",
        "border-info",
        "border-dark",
    ]
    return random.choice(colors)

@register.filter
def get_first_word(value):
    if value:
        words = value.split()
        if words:
            return words[0]
    return ''