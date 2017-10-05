# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_delete_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagem',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
