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
