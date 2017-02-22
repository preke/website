# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_auto_20161114_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsm',
            name='user_name',
            field=models.CharField(default=b'user_name', max_length=50, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d'),
        ),
    ]
