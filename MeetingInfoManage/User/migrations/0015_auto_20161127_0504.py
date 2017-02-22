# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0014_auto_20161127_0502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='demand',
            field=models.CharField(default=b'\xe5\x85\xa8\xe5\x9b\xbd/\xe7\x89\xb9\xe8\x89\xb2\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x8f\x82\xe4\xbc\x9a', max_length=50, verbose_name=b'\xe5\x8f\x82\xe4\xbc\x9a\xe9\x9c\x80\xe6\xb1\x82'),
        ),
    ]
