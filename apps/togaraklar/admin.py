from django.contrib import admin
from .models import *



@admin.register(TogarakList)
class TogarakListAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}

@admin.register(QoshimchaDarsList)
class QoshimchaDarsListAdmin(admin.ModelAdmin):
    list_display = ['title']
    prepopulated_fields = {'slug':('title',)}