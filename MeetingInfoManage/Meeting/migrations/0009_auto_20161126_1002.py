# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Meeting', '0008_meeting_weight_of_participant'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meeting',
            old_name='weight_of_chirman',
            new_name='weight_of_chairman',
        ),
    ]
