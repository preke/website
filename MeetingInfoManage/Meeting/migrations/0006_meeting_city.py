# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0005_auto_20161114_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='city',
            field=models.CharField(default=b'\xe5\xb9\xbf\xe5\xb7\x9e', max_length=100, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x9f\x8e\xe5\xb8\x82', blank=True),
        ),
    ]
