# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='cantidad',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='responsable',
            field=models.ForeignKey(related_name=b'responsable', blank=True, to='inscripciones.Voluntario', null=True),
        ),
    ]
