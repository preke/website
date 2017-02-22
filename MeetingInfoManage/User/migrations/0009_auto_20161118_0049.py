# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0008_client_plan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsm',
            name='members',
            field=models.ManyToManyField(to='User.Client', verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe7\x9a\x84\xe5\xae\xa2\xe6\x88\xb7\xe7\xbe\xa4', blank=True),
        ),
    ]
