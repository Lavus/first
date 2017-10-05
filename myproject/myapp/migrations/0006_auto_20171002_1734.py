# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20171002_1733'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
        migrations.AddField(
            model_name='document',
            name='docfile',
            field=models.FileField(default=datetime.datetime(2017, 10, 2, 20, 34, 8, 700195, tzinfo=utc), upload_to='documents/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]
