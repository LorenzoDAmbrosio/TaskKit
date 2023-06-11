import locale
import random

from django import template
from django.utils import formats

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
    if taskCount == 0 :
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

@register.filter
def format_number(value):
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')

    # Formatta il numero
    formatted_number = locale.format_string("%f", value, grouping=True)    # Do something else here
    return formatted_number