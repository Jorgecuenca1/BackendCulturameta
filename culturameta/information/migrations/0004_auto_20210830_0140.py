# Generated by Django 3.2 on 2021-08-30 06:40

from django.db import migrations, models
import information.models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_city_coro_country_encuestatransparencia_functions_information_mivi_modalidad_nivel_objectives_pqrsd_'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pqrsd',
            name='archivo',
            field=models.FileField(blank=True, null=True, upload_to='pqrsd/file', validators=[information.models.file_size], verbose_name='10.Archivo adjunto'),
        ),
        migrations.AlterField(
            model_name='pqrsd',
            name='asunto',
            field=models.CharField(blank=True, max_length=400, null=True, verbose_name='8.Asunto '),
        ),
        migrations.AlterField(
            model_name='pqrsd',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='pqrsd',
            name='last_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='3.Apellidos del remitente'),
        ),
        migrations.AlterField(
            model_name='pqrsd',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='2.Nombre del remitente'),
        ),
        migrations.AlterField(
            model_name='pqrsd',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='7.Celular'),
        ),
        migrations.AlterField(
            model_name='pqrsd',
            name='solicitud',
            field=models.TextField(blank=True, null=True, verbose_name='9.Descripción Solicitud'),
        ),
    ]
