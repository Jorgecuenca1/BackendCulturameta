from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import Employed, Sede, Information, Objectives, Functions, Coro, Tiposolicitud, Nivel, TypeDocument, Pqrsd, EncuestaTransparencia, Modalidad, Propuesta, Torneo


# Register your models here.
class PatrimonioAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', )
    search_fields = ('id', 'name',  )
    list_filter = ('name',)

class EmployedAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'contact','carge','extension','phone','fax','email', )
    search_fields = ('id', 'name', 'contact','carge','extension','phone','fax','email', )
    list_filter = ('name',)


class SedeAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'type', 'adress','city','phone','fax','email', )
    search_fields = ('id', 'name', 'type', 'adress','city','phone','fax','email',)
    list_filter = ('name',)

class InformationAdmin(ImportExportModelAdmin):
    list_display = ('id', 'meta', 'loft', 'generalities', )
    search_fields = ('id', 'meta', 'loft', 'generalities',)
    list_filter = ('meta',)

class MiViAdmin(ImportExportModelAdmin):
    list_display = ('id', 'mision', 'descriptionmision', 'vision', )
    search_fields = ('id', 'mision', 'descriptionmision', 'vision', )
    list_filter = ('mision',)

class ObjectivesAdmin(ImportExportModelAdmin):
    list_display = ('id', 'objetive', )
    search_fields = ('id', 'objetive',)

class FunctionsAdmin(ImportExportModelAdmin):
    list_display = ('id', 'function' )
    search_fields = ('id', 'function' )
    list_filter = ('function',)
class CoroAdmin(ImportExportModelAdmin):
    list_display = ('id', 'coro' )
    search_fields = ('id', 'coro' )
    list_filter = ('coro',)



@admin.register(Tiposolicitud)
class TiposolicitudAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class TiposolicitudResource(resources.ModelResource):
   class Meta:
    model = Tiposolicitud
@admin.register(Modalidad)
class ModalidadAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class ModalidadResource(resources.ModelResource):
   class Meta:
    model = Modalidad

@admin.register(Propuesta)
class PropuestaAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class PropuestaResource(resources.ModelResource):
   class Meta:
    model = Propuesta

@admin.register(Torneo)
class TorneoAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'email','name', 'agrupacion','seudonimo','type_document', 'identification','expedicion','country', 'region','city', 'adress','phone','phone_movil', 'modalidad','obra1', 'obra2','propuesta','archivo', 'archivo1','link','archivo2','archivo3', 'archivo4',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class TorneoResource(resources.ModelResource):
   class Meta:
    model = Torneo

@admin.register(Nivel)
class NivelAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)
class NivelResource(resources.ModelResource):
   class Meta:
    model = Nivel


@admin.register(TypeDocument)
class TypeDocumentAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'name',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class TypeDocumentResource(resources.ModelResource):
    class Meta:
        model = TypeDocument


@admin.register(Pqrsd)
class PqrsdAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'tiposolicitud','name','last_name','type_document','identification','email','phone','asunto',)
    list_display_links = ('pk',)
    list_editable = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)


class PqrsdResource(resources.ModelResource):
    class Meta:
        model = Pqrsd

@admin.register(EncuestaTransparencia)
class EncuestaTransparenciaAdmin(ImportExportModelAdmin):
    list_display = ('pk', 'encontro','noencontro','facil','nivel','sugerencia',)
    list_display_links = ('pk',)
    list_editable = ('encontro',)
    list_filter = ('encontro',)


class EncuestaTransparenciaResource(resources.ModelResource):
    class Meta:
        model = EncuestaTransparencia
admin.site.register(Employed, EmployedAdmin),
admin.site.register(Patrimonio, PatrimonioAdmin),
admin.site.register(Sede, SedeAdmin),
admin.site.register(Information,InformationAdmin),
admin.site.register(Objectives,ObjectivesAdmin),
admin.site.register(Functions,FunctionsAdmin),
admin.site.register(Coro,CoroAdmin),