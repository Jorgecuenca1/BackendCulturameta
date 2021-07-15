from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Menu


# Register your models here.

class MenuAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('id', 'name','description','price')
    list_filter = ('id',)

admin.site.register(Menu, MenuAdmin),