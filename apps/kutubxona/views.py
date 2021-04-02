from .models import *
from django.views.generic import ListView, DetailView


class ChildrenBookListView(ListView):
    model = ChildrenBook
    context_object_name = 'books'
    template_name = 'kutubxona/children_book.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        link = ChildrenBook.objects.all().order_by('-id')
        table = TableBook.objects.all().order_by('-id')
        context['header_title'] = 'books'
        context = {'table': table, 'link':link}
        return context

    def get_queryset(self):
        return ChildrenBook.objects.filter(is_active=True).order_by('-id')


class ElectronListView(ListView):
    model = Electron
    context_object_name = 'lesson_objects'
    template_name = 'kutubxona/electron-list.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'Electron'
        context['header_title'] = 'Elektron darslik'
        return context

    def get_queryset(self):
        return Electron.objects.filter(published=True).order_by('-id')


class ElectronDetailView(DetailView):
    model = Electron
    template_name = 'kutubxona/electron-detail.html'
    context_object_name = 'lesson'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'Darslik'
        return context


class VideoListView(ListView):
    model = Video
    context_object_name = 'lesson_objects'
    template_name = 'kutubxona/video_list.html'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'Video'
        context['header_title'] = 'Video darslik'
        return context

    def get_queryset(self):
        return Video.objects.filter(published=True).order_by('-id')


class VideoDetailView(DetailView):
    model = Video
    template_name = 'kutubxona/video_detail.html'
    context_object_name = 'lesson'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title_top"] = 'Darslik'
        return context