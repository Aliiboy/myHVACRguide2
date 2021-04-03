from django import template
from utils.menu import get_nodes

register = template.Library()


@register.simple_tag
def dashboard_navigation(user):
    return get_nodes(user)
