from django.db import models

# Create your models here.


from django_file_validator.validators import MaxSizeValidator
from django.core.exceptions import ValidationError

def file_size(value): # add this to some file where you can import it from
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')

# Create your models here.

class Employed(models.Model):
    name=models.CharField(
        null=False,blank=False,max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    contact = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Contacto",
        help_text="Contacto",
    )
    carge = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Cargo",
        help_text="Cargo",
    )
    extension = models.TextField(
        null=False, blank=False,
        verbose_name="Extension telefono",
        help_text="Extension telefono",
    )
    phone = models.IntegerField(
        null=False, blank=False,
        verbose_name="Telefono",
        help_text="Telefono",
    )
    fax = models.CharField(
        null=False, blank=False, max_length=20,
        verbose_name="Fax",
        help_text="Fax",
    )
    email = models.EmailField(
        null=False, blank=False,
        verbose_name="Correo electronico",
        help_text="Correo electronico",
    )

    class Meta:
        ordering=["id"]
        verbose_name="Empleado",
        verbose_name_plural="Empleados"

    def __str__(self):
        return self.name



class Sede(models.Model):
    name=models.CharField(
        null=False,blank=False,max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    type = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Tipo de sede",
        help_text="Tipo de sede",
    )
    adress = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Direccion",
        help_text="Direccion",
    )
    city = models.TextField(
        null=False, blank=False,
        verbose_name="Municipio",
        help_text="Municipio",
    )
    phone = models.IntegerField(
        null=False, blank=False,
        verbose_name="Telefono",
        help_text="Telefono",
    )
    fax = models.CharField(
        null=False, blank=False, max_length=20,
        verbose_name="Fax",
        help_text="Fax",
    )
    email = models.EmailField(
        null=False, blank=False,
        verbose_name="Correo electronico",
        help_text="Correo electronico",
    )

    class Meta:
        ordering=["id"]
        verbose_name="Sede",
        verbose_name_plural="Sede"

    def __str__(self):
        return self.name

class Information(models.Model):
    meta = models.TextField(
        null=True, blank=True,
        verbose_name="Meta",
        help_text="Meta",
    )
    loft = models.TextField(
        null=True, blank=True,
        verbose_name="Altillanura",
        help_text="Altillanura",
    )
    generalities = models.TextField(
        null=True, blank=True,
        verbose_name="Generalidades",
        help_text="Generalidades",
    )
    location = models.TextField(
        null=True, blank=True,
        verbose_name="Localizacion",
        help_text="Localizacion",
    )
    limits = models.TextField(
        null=True, blank=True,
        verbose_name="limites",
        help_text="limites",
    )
    aspects = models.TextField(
        null=True, blank=True,
        verbose_name="Aspectos",
        help_text="Aspectos",
    )
    economy = models.TextField(
        null=True, blank=True,
        verbose_name="Economia",
        help_text="Economia",
    )
    territory = models.TextField(
        null=True, blank=True,
        verbose_name="Territorio",
        help_text="Territorio",
    )
    height = models.TextField(
        null=True, blank=True,
        verbose_name="Altura",
        help_text="Altura",
    )
    temperature = models.TextField(
        null=True, blank=True,
        verbose_name="Temperatura",
        help_text="Temperatura",
    )
    regions = models.TextField(
        null=True, blank=True,
        verbose_name="Regiones",
        help_text="Regiones",
    )
    hydrography = models.TextField(
        null=True, blank=True,
        verbose_name="Informaci??n",
        help_text="Informaci??n",
    )

    def __str__(self):
        return self.meta

class Objectives(models.Model):
    objetive = models.TextField(
        null=True, blank=True,
        verbose_name="Objetivo",
        help_text="Objetivo",
    )


    def __str__(self):
        return self.objetive


class MiVi(models.Model):
    mision = models.CharField(
        null=True, blank=True, max_length=20,
        verbose_name="Mision",
        help_text="Mision",
    )
    descriptionmision = models.TextField(
        null=True, blank=True,
        verbose_name="Descripci??n mision",
        help_text="Descripci??n mision",
    )
    vision = models.CharField(
        null=True, blank=True, max_length=20,
        verbose_name="Vision",
        help_text="Vision",
    )
    descriptionvision = models.TextField(
        null=True, blank=True,
        verbose_name="Descripci??n Vision",
        help_text="Descripci??n Vision",
    )


    def __str__(self):
        return self.mision

class Functions(models.Model):
    function = models.TextField(
        null=True, blank=True,
        verbose_name="Funci??n",
        help_text="Funci??n",
    )


    def __str__(self):
        return self.function

class Coro(models.Model):
    coro = models.TextField(
        null=True, blank=True,
        verbose_name="Coro",
        help_text="Coro",
    )


    def __str__(self):
        return self.coro


BOOLEAN_CHOICES = (
        ('SI', 'SI',),
        ('NO', 'NO',),

    )
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='Nombre del pa??s', max_length=254)
    phone_code = models.CharField(verbose_name='C??digo n??mero telef??nico', max_length=5)

    class Meta:
        verbose_name = 'Pa??s'
        verbose_name_plural = 'Paises'

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(verbose_name='Nombre del departamento', max_length=254)

    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name='Pa??s')

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __str__(self):
        return '{} | {}'.format(self.country.name, self.name)


class City(models.Model):

    name = models.CharField(verbose_name='Nombre municipio', max_length=254)
    state = models.ForeignKey(Region, on_delete=models.PROTECT, verbose_name='Departamento')

    class Meta:
        verbose_name = 'Municipio'
        verbose_name_plural = 'Municipios'

    def __str__(self):
        return '{} | {} | {}'.format(self.state.country.name, self.state.name, self.name)

    def save(self, *args, **kwargs):
        super(City, self).save(*args, **kwargs)

class Propuesta(models.Model):
    name = models.CharField(max_length=120, blank=True, verbose_name='Propuesta')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Propuesta'
        verbose_name_plural = 'Propuesta'

class Modalidad(models.Model):
    name = models.CharField(max_length=120, blank=True, verbose_name='Modalidad')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Modalidad'
        verbose_name_plural = 'Modalidad'
class Tiposolicitud(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de solicitud')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de solicitud'
        verbose_name_plural = 'TIpo de solicitud'



class Nivel(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Nivel')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Nivel'
        verbose_name_plural = 'Nivel'

class Patrimonio(models.Model):
    name = models.CharField(max_length=700, blank=True, verbose_name='Titulo', null=True)
    subtituilo = models.CharField(max_length=700, blank=True, verbose_name='Subtitulo', null=True)
    autor = models.CharField(max_length=700, blank=True, verbose_name='Autor', null=True)
    ano = models.CharField(max_length=700, blank=True, verbose_name='fecha nacimienautor', null=True)
    colaboradores = models.TextField(
        verbose_name='Colaboradores', null=True,
        blank=True)
    tipomaterial = models.CharField(max_length=700, blank=True, verbose_name='Tipo de material', null=True)
    numeropaginas = models.CharField(max_length=700, blank=True, verbose_name='NUmero de paginas', null=True)
    caracteristicas = models.TextField(blank=True, verbose_name='Otras caracteristicas', null=True)
    dimensiones = models.CharField(max_length=700, blank=True, verbose_name='Dimensiones', null=True)
    tiporegistro = models.CharField(max_length=700, blank=True, verbose_name='Tiporegistro', null=True)
    nivelbibliografico = models.CharField(max_length=700, blank=True, verbose_name='Nivel bibliografico', null=True)
    fuentecatalogacion = models.CharField(max_length=700, blank=True, verbose_name='FUENTE DE CATALOGACION', null=True)
    idioma = models.CharField(max_length=700, blank=True, verbose_name='Idioma', null=True)
    edicion = models.CharField(max_length=700, blank=True, verbose_name='Edicion', null=True)
    descripcion = models.TextField(
        verbose_name='Descripci??n', null=True,
        blank=True)
    tipocontenido = models.TextField(
        verbose_name='Tipo de contenido', null=True,
        blank=True)
    isbn = models.CharField(max_length=700, blank=True, verbose_name='ISBN', null=True)
    temas = models.CharField(max_length=700, blank=True, verbose_name='Temas', null=True)
    otraclasificacion = models.CharField(max_length=700, blank=True, verbose_name='Otra Clasificaci??n', null=True)
    breve = models.TextField(
        verbose_name='Breve Descripci??n', null=True,
        blank=True)
    detalle = models.TextField(
        verbose_name='Detalles de adquisici??n', null=True,
        blank=True)
    editorial = models.CharField(max_length=700, blank=True, verbose_name='Editorial', null=True)
    ciudad = models.CharField(max_length=700, blank=True, verbose_name='Ciudad', null=True)
    copias = models.CharField(max_length=700, blank=True, verbose_name='Copias', null=True)
    url = models.CharField(max_length=700, blank=True, verbose_name='Url koha', null=True)
    archivo = models.CharField(max_length=700, blank=True, verbose_name='Url archivo', null=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Catalogo de patrimonio'
        verbose_name_plural = 'Catalogo de Patrimonio'

class TypeDocument(models.Model):
    name = models.CharField(max_length=30, blank=True, verbose_name='Tipo de documento')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'TIpo de documentos'

class Pqrsd(models.Model):
    tiposolicitud = models.ForeignKey(Tiposolicitud, verbose_name='1.Tipo de solicitud', on_delete=models.PROTECT, blank=True, null=True)

    name = models.CharField(max_length=200, blank=True, verbose_name='2.Nombre del remitente', null=True)
    last_name = models.CharField(max_length=200, blank=True, verbose_name='3.Apellidos del remitente', null=True)
    type_document = models.ForeignKey(TypeDocument, verbose_name='4.Tipo de documento',
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    identification = models.CharField(max_length=30, verbose_name='5.Identificaci??n', blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, verbose_name='6.Municipio', null=True)
    email = models.EmailField(max_length=30, blank=True, verbose_name='7.Correo electr??nico', null=True)
    phone = models.CharField(max_length=30, verbose_name='8.Celular', blank=True, null=True)
    asunto = models.CharField(max_length=400, blank=True, verbose_name='9.Asunto ', null=True)
    solicitud = models.TextField(
                                 verbose_name='10.Descripci??n Solicitud', null=True,
                                 blank=True)
    archivo = models.FileField(verbose_name='11.Archivo adjunto', upload_to='pqrsd/file', blank=True, null=True, validators=[file_size])
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Informe PQRSD'
        verbose_name_plural = 'Informe PQRSD'


class EncuestaTransparencia(models.Model):
    encontro = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                   verbose_name='1. Encontr?? la informaci??n que buscaba?:',
                                   null=True,
                                   blank=True)
    noencontro= models.CharField(max_length=100, blank=True, verbose_name='2. Si no la encontr?? especifique en este espacio ??qu?? buscaba?', null=True)
    facil = models.CharField(max_length=2, choices=BOOLEAN_CHOICES,
                                verbose_name='3. ??Le result?? f??cil la ruta de acceso a la informaci??n?:',
                                null=True,
                                blank=True)
    nivel = models.ForeignKey(Nivel, verbose_name='4. ??A nivel general, c??mo define la informaci??n contenida en la p??gina web?',
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    sugerencia = models.CharField(max_length=100, blank=True, verbose_name='5. Si tiene alguna sugerencia escribanos en el siguiente espacio, recuerde que su opini??n es muy importante para mejorar nuestro servicio.', null=True)

    def __str__(self):
        return self.sugerencia

    class Meta:
        verbose_name = 'Encuesta de satisfacci??n'
        verbose_name_plural = 'Encuesta de satisfacci??n'

class Torneo(models.Model):
    email = models.EmailField(max_length=20, blank=True, verbose_name='Correo *', null=True)
    name = models.CharField(max_length=100, blank=True, verbose_name='Nombres y Aepllidos del integrante de la agrupaci??n que har?? las veces de representante (si aplica) y/0 participante: *', null=True)
    agrupacion = models.CharField(max_length=100, blank=True, verbose_name='Nombre de la agrupaci??n (si aplica)', null=True)
    seudonimo = models.CharField(max_length=100, blank=True, verbose_name='Seud??nimo (si aplica):', null=True)
    type_document = models.ForeignKey(TypeDocument, verbose_name='Tipo de identificaci??n: *',
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    identification = models.CharField(max_length=100, verbose_name='N??mero de identificaci??n: *', blank=True, null=True)
    expedicion = models.CharField(max_length=100, verbose_name='Lugar de Expedici??n: *', blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, verbose_name='Pa??s de residencia: *', null=True)
    region = models.CharField(max_length=100, blank=True, verbose_name='Ciudad de residencia: *', null=True)
    city = models.CharField(max_length=100, blank=True, verbose_name='Municipio', null=True)

    adress = models.CharField(max_length=100, blank=True, verbose_name='Direcci??n residencia:', null=True)
    phone = models.CharField(max_length=100, blank=True, verbose_name='Tel??fono fijo:', null=True)
    phone_movil = models.CharField(max_length=100, blank=True, verbose_name='Tel??fono celular: *', null=True)
    modalidad = models.ForeignKey(Modalidad, verbose_name='Modalidad en la que participar??: *',
                                      on_delete=models.PROTECT,
                                      blank=True, null=True)
    obra1 = models.CharField(max_length=100, blank=True, verbose_name='Escriba el nombre de la obra N??1 y/o arreglo que presentar?? al concurso seg??n lo solicitado en las bases: (No Aplica para las modalidades de, Pareja de Baile y Copleros). ', null=True)
    obra2 = models.CharField(max_length=100, blank=True, verbose_name='Escriba el nombre de la obra N??2 y/o arreglo que presentar?? al concurso seg??n lo solicitado en las bases: (No Aplica para las modalidades de, Pareja de Baile y Copleros).', null=True)
    propuesta = models.ForeignKey(Propuesta, verbose_name='Propuesta: *',
                                  on_delete=models.PROTECT,
                                  blank=True, null=True)
    archivo = models.FileField(verbose_name='Seleccione una foto art??stica haciendo clic en agregar archivo - Por favor ADJUNTE una fotograf??a art??stica digital ya sea a color o blanco y negro tama??o m??nimo 800 x 600 Pixeles en una resoluci??n m??nima de 200 dpi.', upload_to='torneo/file', blank=True, null=True, validators=[file_size])
    archivo1 = models.FileField(verbose_name='Cargar el Formulario N??1 - Inscripci??n al 53?? Torneo Internacional del Joropo "MIGUEL ??NGEL MART??N" totalmente diligenciado con los siguientes documentos: Fotocopias de la C??dula ciudadan??a, extranjer??a y/o pasaporte del representante y de los integrantes seg??n sea la modalidad y la certificaci??n de residencia de m??nimo 3 a??os emitida por la Alcald??a del municipio respectivo, o las juntas de acci??n comunal. (aplica solo para los participantes que se presenten por el departamento del Meta). Lo anterior se Adjunta en un solo archivo en formato PDF. *', upload_to='torneo/file', blank=True, null=True, validators=[file_size])
    link = models.CharField(max_length=100, blank=True, verbose_name='Adjuntar el link del archivo de wetranfer donde envia el audio formato punto wav, mp3 etc... y v??deo y/o videos (m??nimo una c??mara m??ximo tres c??maras grabando simult??neamente) FHD, 1080p o superior de la propuesta seg??n sea la modalidad seleccionada: *', null=True)
    archivo2 = models.FileField(verbose_name='sdsd', upload_to='torneo/file', blank=True, null=True, validators=[file_size])
    archivo3 = models.FileField(verbose_name=' Los participantes de las modalidades de Conjunto de M??sica Tradicional llanera y/o Ensambles Nuevos Formatos deber??n enviar una breve, pero s??lida justificaci??n escrita de su obra, que incluya: Datos de la obra (forma y estilo), intenci??n y/o concepto musical desarrollado y argumentar el ??Porqu??? del repertorio seleccionado. Esta podr?? ser utilizada para presentar la obra ante el p??blico por redes y medios de comunicaci??n. Adjuntar el documento en un solo PDF. ', upload_to='torneo/file', blank=True, null=True, validators=[file_size])
    archivo4 = models.FileField(verbose_name='Los participantes de las modalidades de Golpe In??dito, Pasaje In??dito, Poema In??dito, deber??n enviar una (1) copia del texto de la obra, escrita en computador en letra Arial 12, marcada y firmada ??nicamente con el seud??nimo del compositor. Adjuntar el documento en un solo PDF.  ', upload_to='torneo/file', blank=True, null=True, validators=[file_size])
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Torneo del joropo'
        verbose_name_plural = 'Torneo del joropo'
