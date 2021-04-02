from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from . import models



admin.site.register(models.ChildrenBook)
admin.site.register(models.TableBook)
