from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.views.generic import ListView, DetailView
from django.views import View


class OMVListView(ListView):
    model = OMV
    context_object_name = 'omv'
    template_name = 'matbuot/yangilik/omv.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'Biz haqimizda'
        context['header_title'] = 'ommaviy'
        return context

    def get_queryset(self):
        return OMV.objects.filter(published=True).order_by('-id')


class OMVDetailView(DetailView):
    model = OMV
    template_name = 'matbuot/yangilik/omv_detail.html'
    context_object_name = 'omv_detail'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'Ommaviy'
        return context


class YangilikView(ListView):
    model = Yangiliklar
    context_object_name = 'yangilik'
    template_name = 'matbuot/yangilik/yangilik.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'Yangiliklar'
        context['header_title'] = 'Yangiliklar'
        return context

    def get_queryset(self):
        return Yangiliklar.objects.filter(published=True).order_by('-id')


class YangilikDetail(DetailView):
    model = Yangiliklar
    template_name = 'matbuot/yangilik/toliq.html'
    context_object_name = 'yangilik'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'Yangilik'
        return context


class KategoriyaList(ListView):
    model = Yangiliklar
    template_name = 'matbuot/yangilik/kategoriya.html'
    context_object_name = 'yangilik'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'Yangilik'
        return context

    def get_queryset(self):
        return Yangiliklar.objects.filter(category__slug=self.kwargs['slug'], published=True).order_by('category')


class GalleryListView(View):
    template_name = 'matbuot/gallery_list.html'

    def get(self, request):
        context = {"categories": None}
        try:
            qs_category = Category.objects.all()
            context['categories'] = qs_category
        except ObjectDoesNotExist:
            context['categories'] = []
        return render(request=request, template_name=self.template_name, context=context)


class CategoryImageList(View):
    template_name = 'matbuot/gallery_detail.html'

    def get(self, request, title=None):
        category = Category.objects.all()
        qs_image = CategoryImage.objects.filter(category__title=title)
        context = {"images": qs_image, "categories": category}
        return render(request=request, template_name=self.template_name, context=context)


def baseview(request):
    msg = ''
    return HttpResponseRedirect(msg)
