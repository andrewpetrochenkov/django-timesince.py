from django.template import Library
from django.utils.timesince import timesince as _timesince


register = Library()


@register.filter
def timesince(d):
    if not d:
        return ''
    return _timesince(d).split(',')[0]
