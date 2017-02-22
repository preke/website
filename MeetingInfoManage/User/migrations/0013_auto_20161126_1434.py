# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0011_auto_20161126_1434'),
        ('User', '0012_auto_20161126_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='attend',
            field=models.ManyToManyField(related_name='client_attend_set', verbose_name=b'\xe5\x8f\x82\xe5\x8a\xa0\xe7\x9a\x84\xe4\xbc\x9a\xe8\xae\xae', to='Meeting.Meeting', blank=True),
        ),
        migrations.AddField(
            model_name='client',
            name='plan',
            field=models.ManyToManyField(related_name='client_plan_set', verbose_name=b'\xe5\xbe\x85\xe5\x8f\x82\xe5\x8a\xa0\xe4\xbc\x9a\xe8\xae\xae', to='Meeting.Meeting'),
        ),
    ]
