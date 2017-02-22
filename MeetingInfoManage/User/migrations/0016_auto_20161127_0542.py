# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0015_auto_20161127_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='birth',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe5\x87\xba\xe7\x94\x9f\xe5\xb9\xb4\xe6\x9c\x88', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(default=b'*****@163.cpm', max_length=50, null=True, verbose_name=b'E-mail', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='institute_job',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe5\xad\xa6\xe4\xbc\x9a\xe4\xbb\xbb\xe8\x81\x8c', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='job',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe8\x81\x8c\xe5\x8a\xa1', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='major',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe4\xb8\x93\xe4\xb8\x9a', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='office',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe7\xa7\x91\xe5\xae\xa4', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=20, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='purpose',
            field=models.TextField(default=b'\xe5\xbb\xba\xe7\xab\x8b\xe5\x90\x88\xe4\xbd\x9c\xe8\x81\x94\xe7\xb3\xbb', verbose_name=b'\xe5\x8f\x82\xe4\xb8\x8e\xe6\xb4\xbb\xe5\x8a\xa8\xe7\x9b\xae\xe7\x9a\x84', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='represent',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xbb\xa3\xe8\xa1\xa8', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='sex',
            field=models.CharField(default=b'\xe6\x80\xa7\xe5\x88\xab', max_length=10, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='strong_point',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=250, verbose_name=b'\xe7\x89\xb9\xe9\x95\xbf', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='title',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe8\x81\x8c\xe7\xa7\xb0', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='type',
            field=models.CharField(default=b'\xe4\xb8\xb4\xe5\xba\x8a', max_length=50, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b', blank=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='unit',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d', blank=True),
        ),
    ]
