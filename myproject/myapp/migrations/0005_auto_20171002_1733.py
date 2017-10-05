# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20171002_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='docfile',
        ),
        migrations.AddField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=200, blank=True, verbose_name='Title (optional)'),
        ),
    ]
