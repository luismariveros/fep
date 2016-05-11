# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inscripciones', '0008_parroquia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voluntario',
            name='grupo',
        ),
    ]
