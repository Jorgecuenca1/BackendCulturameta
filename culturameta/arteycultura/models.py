from django.db import models
from django.utils import timezone
# Create your models here.
from datetime import *
class Artista(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre",
        help_text="Nombre del Artista",
    )
    last_name = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Apellidos",
        help_text="Apellidos del Artista",
    )
    age = models.PositiveBigIntegerField(
        null=True, blank=True,
        verbose_name="Edad",
        help_text="Edad",
    )
    cedula = models.PositiveBigIntegerField(
        null=True, blank=True,
        verbose_name="Cedula",
        help_text="Cedula",
    )
    lugar_nacimiento = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Lugar de nacimiento",
        help_text="Lugar de nacimiento",
    )
    class Meta:
        ordering = ["id"]
        verbose_name = "Artista",
        verbose_name_plural = "Artista"

    def __str__(self):
        return self.name




class Obra(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    name_obra = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Nombre de la obra",
        help_text="Nombre de la obra",
    )
    artista = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Nombre del artista",
        help_text="Nombre del artista",
    )
    ubicacion = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre de archivo",
        help_text="Nombre de archivo",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    image = models.ImageField(
        null=True, blank=True, max_length=200,
        verbose_name="Imagen ",
        help_text="Imagen ",
    )


    class Meta:
        ordering = ["id"]
        verbose_name = "Obra",
        verbose_name_plural = "Obras"

    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    information = models.TextField(
        null=True, blank=True,
        verbose_name="Informacion",
        help_text="Informacion",
    )
    tittle1 = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Titulo  ",
        help_text="Titulo ",
    )


    description1 = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    tittle2 = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Titulo  ",
        help_text="Titulo ",
    )

    description2 = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    icono= models.ImageField(
        null=True, blank=True, max_length=200,
        verbose_name="Icono ",
        help_text="Icono",
    )
    history = models.TextField(
        null=True, blank=True,
        verbose_name="Historia",
        help_text="Historia",
    )


    class Meta:
        ordering = ["id"]
        verbose_name = "Area",
        verbose_name_plural = "Areas"

    def __str__(self):
        return self.name


class Biblioteca(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    libro = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Libro",
        help_text="Libro",
    )
    librarian = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Bibliotecario",
        help_text="Bibliotecario",
    )
    adress = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Dirección",
        help_text="Dirección",
    )
    zone = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="ZOna",
        help_text="ZOna",
    )
    resolution = models.CharField(
        null=True, blank=True, max_length=200,
        verbose_name="Resolucion",
        help_text="Resolucion",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    history = models.TextField(
        null=True, blank=True,
        verbose_name="Historia",
        help_text="Historia",
    )
    orden = models.PositiveBigIntegerField(
        null=True, blank=True,
        verbose_name="Orden",
        help_text="Orden",
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Biblioteca",
        verbose_name_plural = "Biblioteca"

    def __str__(self):
        return self.name

class Festival(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    descripcion = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Descripción",
        help_text="Descripción",
    )

    orden = models.PositiveBigIntegerField(
        null=True, blank=True,
        verbose_name="Orden",
        help_text="Orden",
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Festival",
        verbose_name_plural = "Festival"

    def __str__(self):
        return self.name

class Noticia(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=400,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    url = models.CharField(
        null=True, blank=True, max_length=400,
        verbose_name="Url ver mas",
        help_text="Url ver mas",
    )

    descripcion = models.TextField(
        null=True, blank=True,
        verbose_name="Descripción",
        help_text="Descripción",
    )

    orden = models.PositiveBigIntegerField(
        null=True, blank=True,
        verbose_name="Orden",
        help_text="Orden",
    )
    file = models.FileField(
        verbose_name='URL Document',
        upload_to=' noticia/imagen',
        blank=True, null=True
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Noticia",
        verbose_name_plural = "Noticia"

    def __str__(self):
        return self.name