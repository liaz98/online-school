from django.shortcuts import render
from django.views.generic import View, ListView
from .models import Normativ, Qoidalar
from django.core.exceptions import ObjectDoesNotExist
from apps.matbuot.models import Yangiliklar


class Normativs(View):
    template_name = 'qonun/content.html'

    def get(self, request):
        try:
            obj = Normativ.objects.filter(is_active=True).last()
            context = {'query': obj}
        except ObjectDoesNotExist:
            context = {'query': None}
            return render(request, self.template_name, context)

        return render(request, self.template_name, context)


class Qonunlar:
    pass


class DownloadContractFile(View):
    template_name = 'qonun/upload_file.html'

    def get(self, request):
        return render(request, self.template_name)


class UzbekistanView(View):
    template_name = 'qonun/uzbekistan.html'

    def get(self, request):
        context = {"title": "O'zbekiston davlat belgilari"}
        return render(request, self.template_name, context)


class Qoidalar(ListView):
    model = Qoidalar
    template_name = 'qonun/maktab_qoidalari.html'
    context_object_name = 'qoidalar'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Maktab qoidalari'
        return context