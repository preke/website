# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0013_auto_20161126_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='chairman_times_plan',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe4\xb8\xbb\xe5\xb8\xad\xe7\xbb\x9f\xe8\xae\xa1'),
        ),
        migrations.AddField(
            model_name='client',
            name='speecher_times_plan',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe8\xae\xb2\xe8\x80\x85\xe7\xbb\x9f\xe8\xae\xa1'),
        ),
        migrations.AlterField(
            model_name='client',
            name='plan',
            field=models.ManyToManyField(related_name='client_plan_set', verbose_name=b'\xe5\xbe\x85\xe5\x8f\x82\xe5\x8a\xa0\xe4\xbc\x9a\xe8\xae\xae', to='Meeting.Meeting', blank=True),
        ),
    ]
