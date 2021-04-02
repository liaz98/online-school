from django import template
from apps.maktab.models import Sinf

register = template.Library()

@register.inclusion_tag('base/inc/sinflar.html')
def sinflar():
    sinf = Sinf.objects.all()
    return {'sinf':sinf}
