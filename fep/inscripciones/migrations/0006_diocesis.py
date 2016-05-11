# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0005_institucioneducativa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diocesis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100, verbose_name=b'Nombre')),
            ],
            options={
                'verbose_name_plural': 'Di\xf3cesis',
            },
            bases=(models.Model,),
        ),
    ]
