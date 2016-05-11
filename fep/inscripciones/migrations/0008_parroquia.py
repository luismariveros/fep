# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0007_decanato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('decanato', models.ForeignKey(default=None, blank=True, to='inscripciones.Decanato', null=True)),
                ('diocesis', models.ForeignKey(default=None, blank=True, to='inscripciones.Diocesis', null=True)),
            ],
            options={
                'verbose_name_plural': 'Parroquias',
            },
            bases=(models.Model,),
        ),
    ]
