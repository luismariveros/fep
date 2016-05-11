# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0009_remove_voluntario_grupo'),
    ]

    operations = [
        migrations.AddField(
            model_name='voluntario',
            name='decanato',
            field=models.ForeignKey(default=None, blank=True, to='inscripciones.Decanato', null=True, verbose_name=b'Decanato'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='voluntario',
            name='diocesis',
            field=models.ForeignKey(default=None, blank=True, to='inscripciones.Diocesis', null=True, verbose_name=b'Di\xc3\xb3cesis'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='voluntario',
            name='institucion_educativa',
            field=models.ForeignKey(default=None, blank=True, to='inscripciones.InstitucionEducativa', null=True, verbose_name=b'Instituci\xc3\xb3n Educativa'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='voluntario',
            name='movimiento',
            field=models.ForeignKey(default=None, blank=True, to='inscripciones.Movimiento', null=True, verbose_name=b'Movimiento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='voluntario',
            name='parroquia',
            field=models.ForeignKey(default=None, blank=True, to='inscripciones.Parroquia', null=True, verbose_name=b'Parroquia'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='voluntario',
            name='tipo_movilidad',
            field=models.ForeignKey(default=None, blank=True, to='inscripciones.TipoMovilidad', null=True, verbose_name=b'Si posee registro de conducir, que tipo de veh\xc3\xadculo maneja.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='voluntario',
            name='ocupacion',
            field=models.ForeignKey(verbose_name=b'Ocupaci\xc3\xb3n (*)', to='inscripciones.Ocupacion'),
        ),
    ]
