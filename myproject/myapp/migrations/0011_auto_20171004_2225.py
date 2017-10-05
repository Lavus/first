# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20171004_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depoimento',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 5, 1, 25, 8, 764648, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='destaque',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 5, 1, 25, 24, 415039, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagem',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 5, 1, 25, 27, 718750, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imovel',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 5, 1, 25, 34, 205078, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
