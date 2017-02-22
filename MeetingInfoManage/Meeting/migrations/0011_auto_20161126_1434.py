# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0010_meeting_type_of_meeting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='chairman',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='speecher',
        ),
        migrations.AlterField(
            model_name='meeting',
            name='rmm_of_meeting',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'\xe4\xbc\x9a\xe8\xae\xae\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba\xe5\x9c\xb0\xe5\x8c\xba\xe7\xbb\x8f\xe7\x90\x86'),
        ),
    ]
