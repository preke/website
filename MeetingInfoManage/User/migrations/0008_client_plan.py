# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0006_meeting_city'),
        ('User', '0007_auto_20161115_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='plan',
            field=models.ManyToManyField(related_name='client_plan_set', verbose_name=b'\xe5\xbe\x85\xe5\x8f\x82\xe5\x8a\xa0\xe4\xbc\x9a\xe8\xae\xae', to='Meeting.Meeting'),
        ),
    ]
