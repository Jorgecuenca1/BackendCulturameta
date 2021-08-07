from django.db import models

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
        verbose_name="Hidrografía",
        help_text="Hidrografía",
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
        verbose_name="Descripción mision",
        help_text="Descripción mision",
    )
    vision = models.CharField(
        null=True, blank=True, max_length=20,
        verbose_name="Vision",
        help_text="Vision",
    )
    descriptionvision = models.TextField(
        null=True, blank=True,
        verbose_name="Descripción Vision",
        help_text="Descripción Vision",
    )


    def __str__(self):
        return self.mision

class Functions(models.Model):
    function = models.TextField(
        null=True, blank=True,
        verbose_name="Función",
        help_text="Función",
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
