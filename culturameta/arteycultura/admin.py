from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Artista, Obra, Area, Biblioteca, Festival, Noticia


# Register your models here.

class ArtistaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'last_name','age','cedula','lugar_nacimiento')
    search_fields = ('id', 'name', 'last_name','age','cedula','lugar_nacimiento')
    list_filter = ('cedula',)


class ObraAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'name_obra','artista','ubicacion','description')
    search_fields = ('id', 'name', 'name_obra','artista','ubicacion','description')
    list_filter = ('name',)

class AreaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('id', 'name', 'description')
    list_filter = ('name',)

class BibliotecaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'libro','description','orden')
    search_fields = ('id', 'name', 'libro','description','orden')
    list_filter = ('id',)

class FestivalAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'descripcion','orden','fecha')
    search_fields = ('id', 'name', 'descripcion','orden','fecha')
    list_filter = ('id',)

class NoticiaAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'descripcion','orden')
    search_fields = ('id', 'name', 'descripcion','orden')
    list_filter = ('id',)

admin.site.register(Artista, ArtistaAdmin),
admin.site.register(Obra, ObraAdmin),
admin.site.register(Area, AreaAdmin),
admin.site.register(Biblioteca, BibliotecaAdmin),
admin.site.register(Festival, FestivalAdmin),
admin.site.register(Noticia, NoticiaAdmin)