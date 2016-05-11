# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
            ],
            options={
                'verbose_name_plural': 'Ciudades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre (*)')),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email (*)')),
                ('asunto', models.CharField(max_length=100, null=True, verbose_name=b'Asunto', blank=True)),
                ('mensaje', models.TextField(verbose_name=b'Mensaje (*)')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'departamento',
                'verbose_name_plural': 'departamentos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('cantidad', models.PositiveIntegerField()),
                ('grupo_padre', models.ForeignKey(blank=True, to='inscripciones.Grupo', null=True)),
            ],
            options={
                'verbose_name_plural': 'Grupos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('departamento', models.ForeignKey(to='inscripciones.Departamento')),
            ],
            options={
                'ordering': ['nombre'],
                'verbose_name': 'localidad',
                'verbose_name_plural': 'localidades',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MiForm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
            ],
            options={
                'verbose_name_plural': 'Ocupaciones',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
            ],
            options={
                'verbose_name_plural': 'Pa\xedses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombres (*)')),
                ('apellido_paterno', models.CharField(max_length=100, verbose_name=b'Primer Apellido (*)')),
                ('apellido_materno', models.CharField(max_length=100, null=True, verbose_name=b'Segundo Apellido', blank=True)),
                ('sexo', models.CharField(max_length=50, verbose_name=b'Sexo (*)', choices=[(b'M', b'Masculino'), (b'F', b'Femenino')])),
                ('fecha_nacimiento', models.DateField(verbose_name=b'Fecha de Nacimiento (*)')),
                ('telefono', models.CharField(max_length=40, verbose_name=b'Tel\xc3\xa9fono (*)')),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email (*)')),
                ('documento_tipo', models.CharField(max_length=50, verbose_name=b'Tipo de Documento (*)', choices=[(b'CI', b'C\xc3\xa9dula de Identidad'), (b'PA', b'Pasaporte')])),
                ('documento_numero', models.CharField(max_length=100, verbose_name=b'N\xc3\xbamero de Documento (*)')),
                ('documento_vencimiento', models.DateField(verbose_name=b'Fecha de Vencimiento del Documento (*)')),
                ('direccion_residencia', models.CharField(max_length=300, verbose_name=b'Direcci\xc3\xb3n en Pa\xc3\xads de Residencia (*)')),
                ('direccion_paraguay', models.CharField(max_length=300, null=True, verbose_name=b'Direcci\xc3\xb3n en Paraguay', blank=True)),
                ('ocupacion_otros', models.CharField(max_length=100, null=True, verbose_name=b'Otra ocupaci\xc3\xb3n', blank=True)),
                ('fecha_inscripcion', models.DateTimeField(auto_now_add=True)),
                ('direccion_ip', models.IPAddressField(null=True)),
                ('tiene_alguna_discapacidad', models.BooleanField(default=False, verbose_name=b'\xc2\xbfPosee usted alg\xc3\xban tipo de discapacidad?')),
                ('necesita_alojamiento', models.BooleanField(default=False, verbose_name=b'\xc2\xbfNecesita alojamiento?')),
                ('ciudad_residencia', models.ForeignKey(related_name='ciudad_residencia', verbose_name=b' Ciudad de Residencia (*)', blank=True, to='inscripciones.Ciudad', null=True)),
                ('departamento_residencia', models.ForeignKey(related_name='departamento_residencia', verbose_name=b' Departamento de Residencia (*)', blank=True, to='inscripciones.Departamento', null=True)),
                ('documento_pais_emisor', models.ForeignKey(related_name='pais_emisor', verbose_name=b'Pa\xc3\xads Emisor del Documento (*)', to='inscripciones.Pais')),
                ('grupo', models.ForeignKey(blank=True, to='inscripciones.Grupo', null=True)),
                ('localidad_residencia', models.ForeignKey(related_name='localidad_residencia', verbose_name=b' Localidad de Residencia (*)', blank=True, to='inscripciones.Localidad', null=True)),
                ('nacionalidad', models.ForeignKey(related_name='nacionalidad', to='inscripciones.Pais')),
                ('ocupacion', models.ForeignKey(verbose_name=b'Ocupaci\xc3\xb3n', to='inscripciones.Ocupacion')),
                ('pais_residencia', models.ForeignKey(related_name='pais_residencia', verbose_name=b' Pa\xc3\xads de Residencia (*)', to='inscripciones.Pais')),
            ],
            options={
                'verbose_name_plural': 'Voluntarios',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='grupo',
            name='responsable',
            field=models.ForeignKey(related_name='responsable', to='inscripciones.Voluntario'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='departamento',
            name='pais',
            field=models.ForeignKey(to='inscripciones.Pais'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ciudad',
            name='departamento',
            field=models.ForeignKey(default=None, blank=True, to='inscripciones.Departamento', null=True),
            preserve_default=True,
        ),
    ]
