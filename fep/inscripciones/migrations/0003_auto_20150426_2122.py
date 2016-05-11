# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0002_auto_20150426_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoMovilidad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
            ],
            options={
                'verbose_name_plural': 'Tipos de Movilidad',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='cantidad',
            field=models.PositiveIntegerField(default=None, null=True, blank=True),
        ),
    ]
