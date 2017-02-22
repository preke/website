# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0011_auto_20161126_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='is_checked',
            field=models.BooleanField(default=False, verbose_name=b'\xe5\xae\xa1\xe6\xa0\xb8'),
        ),
    ]
