from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from adminsortable2.admin import SortableAdminMixin


class YangiliklarForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Yangiliklar
        fields = '__all__'


class JarayonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Jarayon
        fields = '__all__'


class SinflarAdmin(admin.ModelAdmin):
    list_display = ('title', 'school_news', 'created', 'slug', 'published',)
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'content')
    list_editable = ('published',)
    list_filter = ('published', 'school_news')


class KategoriyaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class YangiliklarAdmin(admin.ModelAdmin):
    form = YangiliklarForm
    list_display = ('title', 'category', 'created', 'slug', 'published',)
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'content')
    list_editable = ('published',)
    list_filter = ('published', 'category')


class JadvalAdmin(admin.ModelAdmin):
    list_display = ('id', 'date')


class TeacherAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('sortings', 'id', 'teacher_name',)


@admin.register(KunTartibi)
class KunTartibiAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('sortings', 'start_time', 'end_time', 'title',)


class ImageGalleryInline(admin.TabularInline):
    model = ImageGallery
    extra = 3


class KitchenInline(admin.TabularInline):
    model = Kitchen


@admin.register(KitchenContent)
class KitchenContentAdmin(admin.ModelAdmin):
    inlines = [ImageGalleryInline, KitchenInline]
    list_display = ('title',)


class ImageCollectionInline(admin.TabularInline):
    model = ImageCollection


class ChoyInline(admin.TabularInline):
    model = Choy


@admin.register(ChoyContent)
class ChoyContentAdmin(admin.ModelAdmin):
    inlines = [ImageCollectionInline, ChoyInline]
    list_display = ('title',)


class JarayonAdmin(admin.ModelAdmin):
    form = JarayonForm
    list_display = ('title', 'created', 'slug', 'published',)
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'content')
    list_editable = ('published',)
    list_filter = ('published', )


admin.site.register(Sinf, SinflarAdmin)
admin.site.register(Kategoriya, KategoriyaAdmin)
admin.site.register(Yangiliklar, YangiliklarAdmin)
admin.site.register(Jarayon, JarayonAdmin)
admin.site.register(DarsJadvali, JadvalAdmin)
admin.site.register(Teacher, TeacherAdmin)
