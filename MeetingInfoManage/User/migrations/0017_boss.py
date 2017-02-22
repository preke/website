# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0016_auto_20161127_0542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boss',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_name', models.CharField(default=b'\xe8\x80\x81\xe6\x9d\xbf', max_length=50, verbose_name=b'\xe8\x80\x81\xe6\x9d\xbf')),
                ('password', models.CharField(default=b'e10adc3949ba59abbe56e057f20f883e', max_length=250, verbose_name=b'\xe5\xaf\x86\xe7\xa0\x81')),
            ],
        ),
    ]
