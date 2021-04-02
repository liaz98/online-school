from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.views.generic import DetailView
from .models import TogarakList, QoshimchaDarsList

class TogarakDetail(DetailView):
    model = TogarakList
    template_name = 'togaraklar/togarak_detail.html'
    context_object_name = 'qr'


def tugarak_home(request):
    msg ='/'
    return HttpResponseRedirect(msg)

class QoshimchaDarsDetail(DetailView):
    model = QoshimchaDarsList
    template_name = 'togaraklar/qoshimchadars_detail.html'
    context_object_name = 'qd'


def qoshimchadars_home(request):
    msg ='qoshimchadars/'
    return HttpResponseRedirect(msg)
