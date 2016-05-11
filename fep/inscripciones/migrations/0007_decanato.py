# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0006_diocesis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Decanato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
                ('diocesis', models.ForeignKey(to='inscripciones.Diocesis')),
            ],
            options={
                'verbose_name_plural': 'Decanatos',
            },
            bases=(models.Model,),
        ),
    ]
