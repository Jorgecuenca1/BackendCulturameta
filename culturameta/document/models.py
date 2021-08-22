import os
import uuid

from django.db import models
from django.core.exceptions import ValidationError

from django_file_validator.validators import MaxSizeValidator

def validate_file_size(value):
    filesize = value.file.size

    if filesize > 2621440:
        raise ValidationError("The maximum file size that can be uploaded is 2.5MB")
    else:
        return value


class Image(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    imagen = models.ImageField(
        null=False, blank=False,
            verbose_name="Imagen ",
        help_text="Imagen ",
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Imagen",
        verbose_name_plural = "Imagen"

    def __str__(self):
        return self.name


class Menu(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Menu",
        verbose_name_plural = "Menu"

    def __str__(self):
        return self.name



class Module(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    menu = models.ForeignKey(
        Menu, on_delete=models.DO_NOTHING,
        verbose_name="Menu",
        help_text="Menu",
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Modulo",
        verbose_name_plural = "Modulo"

    def __str__(self):
        return self.name


class SubModule(models.Model):
    name = models.CharField(
        null=False, blank=False, max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    module = models.ForeignKey(
        Module, on_delete=models.DO_NOTHING,
        verbose_name="Modulo",
        help_text="Modulo",
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Sub modulo",
        verbose_name_plural = "Sub modulo"

    def __str__(self):
        return self.name
def documents_path(instance, filename):

    if instance.submodule is None:
        filename = 'document/{}/{}/{}'.format(instance.module, instance.age, filename)
    else:
        filename = 'document/{}/{}/{}/{}'.format(instance.module, instance.submodule, instance.age, filename)
    # return the whole path to the file
    return filename

class Document(models.Model):

    name = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    name_archive = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Nombre de archivo",
        help_text="Nombre de archivo",
    )
    age = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Año",
        help_text="Año",
    )
    month = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Mes",
        help_text="Mes",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    orden = models.PositiveBigIntegerField(
        null=True, blank=True,
        verbose_name="Orden",
        help_text="Orden",
    )
    module = models.ForeignKey(
        Module, on_delete=models.DO_NOTHING,
        verbose_name="Modulo",
        help_text="Modulo",
        blank=True, null=True
    )
    submodule = models.ForeignKey(
        SubModule, on_delete=models.DO_NOTHING,
        verbose_name="Submodulo",
        help_text="SubModulo",
        blank=True, null=True
    )
    url = models.FileField(
        verbose_name='URL Document',
        upload_to= documents_path,
        blank=True, null=True, validators=[validate_file_size]
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Document",
        verbose_name_plural = "Document"

    def __str__(self):
        return self.name



class Controlinterno(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    name_archive = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Nombre de archivo",
        help_text="Nombre de archivo",
    )
    age = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Año",
        help_text="Año",
    )
    month = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Mes",
        help_text="Mes",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    orden = models.PositiveBigIntegerField(
        null=True, blank=True,
        verbose_name="Orden",
        help_text="Orden",

    )
    module = models.ForeignKey(
        Module, on_delete=models.DO_NOTHING,
        verbose_name="Modulo",
        help_text="Modulo",
        blank=True, null=True
    )
    submodule = models.ForeignKey(
        SubModule, on_delete=models.DO_NOTHING,
        verbose_name="Submodulo",
        help_text="SubModulo",
        blank=True, null=True
    )
    url = models.FileField(
        verbose_name='URL Document',
        upload_to= documents_path,
        blank=True, null=True
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Control Interno",
        verbose_name_plural = "Control Interno"

    def __str__(self):
        return self.name




class Presupuesto(models.Model):
    name = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Nombre ",
        help_text="Nombre ",
    )
    name_archive = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Nombre de archivo",
        help_text="Nombre de archivo",
    )
    age = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Año",
        help_text="Año",
    )
    month = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Mes",
        help_text="Mes",
    )
    description = models.TextField(
        null=True, blank=True,
        verbose_name="Descripcion",
        help_text="Descripcion",
    )
    orden = models.PositiveBigIntegerField(
        null=True, blank=True,
        verbose_name="Orden",
        help_text="Orden",

    )
    module = models.ForeignKey(
        Module, on_delete=models.DO_NOTHING,
        verbose_name="Modulo",
        help_text="Modulo",
        blank=True, null=True
    )
    submodule = models.ForeignKey(
        SubModule, on_delete=models.DO_NOTHING,
        verbose_name="Submodulo",
        help_text="SubModulo",
        blank=True, null=True
    )
    url = models.FileField(
        verbose_name='URL Document',
        upload_to='document/file',
        blank=True, null=True
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Presupuesto",
        verbose_name_plural = "Presupuesto"

    def __str__(self):
        return self.name


class Accountability(models.Model):
    accountability = models.CharField(
        null=True, blank=True, max_length=100,
        verbose_name="Rendición de cuentas ",
        help_text="Rendición de cuentas ",
    )
    url = models.CharField(
        null=True, blank=True, max_length=50,
        verbose_name="Url",
        help_text="Url",
    )

    file = models.FileField(
        verbose_name='URL Document',
        upload_to=' document/rendicion',
        blank=True, null=True
    )

    class Meta:
        ordering = ["id"]
        verbose_name = "Rendicion de cuentas",
        verbose_name_plural = "Rendicion de cuentas"

    def __str__(self):
        return self.accountability
