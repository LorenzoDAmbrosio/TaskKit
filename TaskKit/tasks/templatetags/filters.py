from django import template

register = template.Library()

@register.filter
def is_member_of_community(user, community):
    return user in community.members.all()

@register.filter
def filter_tasks_by_status(tasks,status):
    return tasks.filter(status=status).all()