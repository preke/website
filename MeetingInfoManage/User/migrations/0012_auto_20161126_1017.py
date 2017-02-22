# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_auto_20161126_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='region_manager',
            field=models.ForeignKey(related_name='client_set', verbose_name=b'\xe5\xa4\xa7\xe5\x8c\xba\xe7\xbb\x8f\xe7\x90\x86RSM', blank=True, to='User.RSM', null=True),
        ),
    ]
