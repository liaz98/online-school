from django import template
from django.core.exceptions import ObjectDoesNotExist
from apps.maktab.models import DarsJadvali
from apps.togaraklar.models import TogarakList, QoshimchaDarsList
from apps.home.models import Reklama

register = template.Library()


@register.inclusion_tag('base/inc/sidebar.html')
def sidebar():
    try:
        togarak = TogarakList.objects.all()
        qoshimchadars = QoshimchaDarsList.objects.all()
        qd = QoshimchaDarsList.objects.get(pk=1)
        qr = DarsJadvali.objects.get(pk=1)
        context = {'qr': qr, 'togarak': togarak,'qd': qd, 'qoshimchadars': qoshimchadars }

    except ObjectDoesNotExist:

        togarak = TogarakList.objects.all()
        qd = []
        qr = []
        context = {'qr': qr, 'togarak': togarak, 'qd': qd, 'qoshimchadars': qoshimchadars}
    return context

@register.inclusion_tag('base/inc/reklama.html')
def reklama():
    try:
        reklama = Reklama.objects.all()
        context = {'reklama':reklama}

    except ObjectDoesNotExist:
        reklama = Reklama.objects.all()
        reklama =[]
        context = {'reklama': reklama}

    return context
