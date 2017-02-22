# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0009_auto_20161126_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='type_of_meeting',
            field=models.CharField(default=b'\xe7\xb1\xbb\xe5\x9e\x8b', max_length=100, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
    ]
