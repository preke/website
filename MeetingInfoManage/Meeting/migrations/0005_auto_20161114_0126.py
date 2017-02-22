# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0004_meeting_is_end_up'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='date',
        ),
        migrations.AddField(
            model_name='meeting',
            name='month',
            field=models.CharField(default=b'2', max_length=100, verbose_name=b'\xe6\x9c\x88'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='year',
            field=models.CharField(default=b'2016', max_length=100, verbose_name=b'\xe5\xb9\xb4'),
        ),
    ]
