# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0007_auto_20161126_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='weight_of_participant',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x8f\x82\xe4\xbc\x9a\xe6\x9d\x83\xe9\x87\x8d'),
        ),
    ]
