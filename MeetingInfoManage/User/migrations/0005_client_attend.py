# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0005_auto_20161114_0126'),
        ('User', '0004_auto_20161105_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='attend',
            field=models.ManyToManyField(to='Meeting.Meeting', verbose_name=b'\xe5\x8f\x82\xe5\x8a\xa0\xe7\x9a\x84\xe4\xbc\x9a\xe8\xae\xae', blank=True),
        ),
    ]
