from django.contrib import admin
from .models import Normativ, Qoidalar
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NormativForm(forms.ModelForm):
    content = forms.CharField(widget= CKEditorUploadingWidget())
    title = forms.CharField(widget= CKEditorUploadingWidget())

    class Meta:
        model = Normativ
        fields = '__all__'

# class Maktab_Qoidlari_Form(forms.ModelForm):
#     content = forms.CharField(widget= CKEditorUploadingWidget())
#
#
#     class Meta:
#         model = Maktab_Qoidalari
#         fields = '__all__'

class NormativAdmin(admin.ModelAdmin):
    form = NormativForm
    list_display = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
    list_display_links = ('title','slug')


# class Maktab_Qoidalari_Admin(admin.ModelAdmin):
#     form = Maktab_Qoidlari_Form
#     list_display = ('title','slug')
#     prepopulated_fields = {'slug':('title',)}
#     list_display_links = ('title','slug')

@admin.register(Qoidalar)
class QoidalarAdmin(admin.ModelAdmin):
    list_display = ['id', 'sarlavha']


admin.site.register(Normativ, NormativAdmin)
# admin.site.register(Maktab_Qoidalari, Maktab_Qoidalari_Admin)

