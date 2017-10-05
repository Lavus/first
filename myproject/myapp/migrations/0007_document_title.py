# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20171002_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(blank=True, max_length=200, verbose_name='Title (optional)'),
        ),
    ]
