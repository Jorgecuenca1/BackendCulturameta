from rest_framework import serializers
from .models import Employed, Sede, Information, Objectives, MiVi, Coro, Functions, Patrimonio


class EmployedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employed
        fields = ['name','contact','carge','extension','phone','fax','email',]

class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = ['name','type','adress','city','phone','fax','email',]

class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = ['meta','loft','generalities','location','limits','aspects','economy', 'territory','height','temperature','regions','hydrography']

class ObjectivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Objectives
        fields = ['objetive']

class MiViSerializer(serializers.ModelSerializer):
    class Meta:
        model = MiVi
        fields = ['mision','descriptionmision','vision','descriptionvision',]

class FunctionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Functions
        fields = ['function']

class CoroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coro
        fields = ['coro']

class PatrimonioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patrimonio
        fields = ['name','subtituilo','autor','ano','colaboradores','tipomaterial','numeropaginas','caracteristicas','dimensiones','tiporegistro','nivelbibliografico','fuentecatalogacion','idioma','edicion','descripcion','tipocontenido',
                  'isbn','temas','otraclasificacion','breve','detalle','editorial','ciudad','copias','url','archivo',]