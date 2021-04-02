from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View


class Sinflar(ListView):
    model = Sinf
    context_object_name = 'sinf'
    template_name = 'maktab/sinf.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Sinflar ro`yhati'
        return context


class SinfDetail(DetailView):
    model = Sinf
    context_object_name = 'sinf'
    template_name = 'maktab/toliq.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["yangilik"] = Yangiliklar.objects.filter(category__slug=self.kwargs['slug'], published=True).order_by(
            '-created')[:4]
        return context


class SinfYangilikDetail(DetailView):
    model = Yangiliklar
    template_name = 'maktab/sinf_yangilik_toliq.html'
    context_object_name = 'yangilik'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'title'
        return context


class Jadval(TemplateView):
    template_name = 'maktab/jadval.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = DarsJadvali.objects.get(pk=1)
        return context


class TeacherList(ListView):
    model = Teacher
    template_name = 'maktab/teacher_list.html'
    context_object_name = 'teacher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'O`qituvchilar ro`yhati'
        context['room'] = self.model.objects.all()
        return context


class KunTartibiList(ListView):
    model = KunTartibi
    template_name = 'maktab/kun_tartibi.html'
    context_object_name = 'kun'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Kun Tartibi'
        return context


class KitchenListView(ListView):
    template_name = 'maktab/kitchen.html'
    model = Kitchen

    def get(self, request):
        photos = KitchenContent.objects.all().first()
        images = ImageGallery.objects.all().order_by('-id')
        items = Kitchen.objects.all().order_by('-id')
        paginator = Paginator(items, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'images':images, 'photos': photos, 'items':page_obj, "title": "Oshxona"}
        return render(request, self.template_name, context)



class KitchenDetailView(View):
    template_name = 'maktab/kitchen_detail.html'

    def get(self, request, pk):
        items = Kitchen.objects.filter(pk=pk)
        context = {"items": items, "title": f"Haftalik taomnoma {items.first().date}"}
        return render(request, self.template_name, context)


class ChoyListView(ListView):
    template_name = 'maktab/choy.html'
    model = Choy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'Choy'
        context['header_title'] = 'Choy'
        items = Choy.objects.all().order_by('-id')
        photos = ChoyContent.objects.all().first()
        images = ImageCollection.objects.all().order_by('-id')
        context = {'images': images, 'photos': photos, "items": items, "title": "Tolmas Choy"}
        return context


class ChoyDetailView(View):
    template_name = 'maktab/choy_detail.html'

    def get(self, request, pk):
        items = Choy.objects.filter(pk=pk)
        context = {"items": items, "title": f"Tolmas choy {items.first().date}"}
        return render(request, self.template_name, context)


class JarayonListView(ListView):
    model = Jarayon
    context_object_name = 'jarayon'
    template_name = 'maktab/jarayon-list.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'Yangiliklar'
        context['header_title'] = 'Yangiliklar'
        return context

    def get_queryset(self):
        return Jarayon.objects.filter(published=True).order_by('-id')


class JarayonDetail(DetailView):
    model = Jarayon
    template_name = 'maktab/jarayon-detail.html'
    context_object_name = 'jarayon'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'JARAYON'
        return context
