from django import template
from django.template.defaultfilters import stringfilter
register = template.Library()

from django import template

@register.filter
def multiply(value, arg):
    return value * arg