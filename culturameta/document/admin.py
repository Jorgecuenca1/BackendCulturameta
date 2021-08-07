from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Image, Menu, Module, SubModule, Document, Accountability


# Register your models here.

class ImageAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('id', 'name',)
    list_filter = ('id',)


class MenuAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('id', 'name', )
    list_filter = ('name',)

class ModuleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name','menu')
    search_fields = ('id', 'name', 'menu')
    list_filter = ('name',)

class SubModuleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'module')
    search_fields = ('id', 'name', 'module')
    list_filter = ('id','name')

class DocumentAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'name_archive','description','orden','module','submodule','url')
    search_fields = ('id', 'name', 'name_archive','description','orden','module','submodule','url')
    list_filter = ('id',)

class AccountabilityAdmin(ImportExportModelAdmin):
    list_display = ('id', 'accountability', 'file')
    search_fields = ('id', 'name')
    list_filter = ('id',)


admin.site.register(Image, ImageAdmin),
admin.site.register(Menu, MenuAdmin),
admin.site.register(Module, ModuleAdmin),
admin.site.register(SubModule, SubModuleAdmin),
admin.site.register(Document, DocumentAdmin),
admin.site.register(Accountability, AccountabilityAdmin),