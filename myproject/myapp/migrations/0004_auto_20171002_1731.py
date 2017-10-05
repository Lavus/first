# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20171002_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='title',
        ),
        migrations.AddField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='documents/%Y/%m/%d', default=datetime.datetime(2017, 10, 2, 20, 31, 44, 481445, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
