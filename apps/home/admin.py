from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import *



@admin.register(Aloqa)
class AloqaAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'second_phone', 'adress']
    list_editable = ['phone', 'second_phone']

class FatherAndMotherForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = FatherAndMother
        fields = '__all__'

@admin.register(Savollar)
class SavollarAdmin(admin.ModelAdmin):
    list_display = ['id', 'savol']


@admin.register(FatherAndMother)
class FatherAndMotherAdmin(admin.ModelAdmin):
    form = FatherAndMotherForm
    list_display = ('title', 'created', 'slug', 'published',)
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'content')
    list_editable = ('published',)
    list_filter = ('published', )

@admin.register(Reklama)
class ReklamaAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']
