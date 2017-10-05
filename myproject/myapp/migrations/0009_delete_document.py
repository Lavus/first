# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20171002_1955'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
    ]
