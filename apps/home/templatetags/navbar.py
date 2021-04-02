from django import template
from apps.maktab.models import Sinf

register = template.Library()


@register.inclusion_tag('base/navbar.html')
def navbar():
    sinf_nav = Sinf.objects.all()
    context = {'sinf_nav': sinf_nav, }
    return context
