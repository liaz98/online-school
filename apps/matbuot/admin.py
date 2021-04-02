from django.contrib import admin
from .models import *
from adminsortable2.admin import SortableAdminMixin


class YangilikAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created', 'slug', 'published',)
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'content')
    list_editable = ('published',)
    list_filter = ('published', 'category')


class OMVAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'slug', 'published',)
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('title', 'slug')
    search_fields = ('title', 'content')
    list_editable = ('published',)
    list_filter = ('published', )


class KategoriyaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Category)
class GalleryCategoryAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'title', 'sortings', 'image')
    # prepopulated_fields = {'slug':('title',)}


@admin.register(CategoryImage)
class GallerySuratiAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('id', 'sortings', 'image')
    # prepopulated_fields = {'slug': ('title',)}


admin.site.register(Yangiliklar, YangilikAdmin)
admin.site.register(Kategoriya, KategoriyaAdmin)
admin.site.register(OMV, OMVAdmin)
