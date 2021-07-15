from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Employed, Sede


# Register your models here.

class EmployedAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'contact','carge','extension','phone','fax','email', )
    search_fields = ('id', 'name', 'contact','carge','extension','phone','fax','email', )
    list_filter = ('name',)


class SedeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'type', 'adress','city','phone','fax','email', )
    search_fields = ('id', 'name', 'type', 'adress','city','phone','fax','email',)
    list_filter = ('name',)


admin.site.register(Employed, EmployedAdmin),
admin.site.register(Sede, SedeAdmin),