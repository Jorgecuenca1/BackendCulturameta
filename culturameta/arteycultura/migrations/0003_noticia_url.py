# Generated by Django 3.2 on 2021-08-30 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arteycultura', '0002_auto_20210829_2347'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='url',
            field=models.CharField(blank=True, help_text='Url ver mas', max_length=400, null=True, verbose_name='Url ver mas'),
        ),
    ]