# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0010_auto_20161118_0501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='attend',
        ),
        migrations.RemoveField(
            model_name='client',
            name='plan',
        ),
        migrations.RemoveField(
            model_name='rsm',
            name='members',
        ),
        migrations.AddField(
            model_name='client',
            name='max_potential_weight',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x9b\xba\xe5\xae\x9a\xe5\xae\xa2\xe6\x88\xb7\xe6\x9d\x83\xe9\x87\x8d'),
        ),
        migrations.AlterField(
            model_name='client',
            name='birth',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe5\x87\xba\xe7\x94\x9f\xe5\xb9\xb4\xe6\x9c\x88'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(default=b'*****@163.cpm', max_length=50, null=True, verbose_name=b'E-mail'),
        ),
        migrations.AlterField(
            model_name='client',
            name='institute_job',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe5\xad\xa6\xe4\xbc\x9a\xe4\xbb\xbb\xe8\x81\x8c'),
        ),
        migrations.AlterField(
            model_name='client',
            name='job',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe8\x81\x8c\xe5\x8a\xa1'),
        ),
        migrations.AlterField(
            model_name='client',
            name='major',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe4\xb8\x93\xe4\xb8\x9a'),
        ),
        migrations.AlterField(
            model_name='client',
            name='office',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe7\xa7\x91\xe5\xae\xa4'),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=20, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba'),
        ),
        migrations.AlterField(
            model_name='client',
            name='potential_weight',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\xbd\x93\xe5\x89\x8d\xe5\xae\xa2\xe6\x88\xb7\xe6\xbd\x9c\xe5\x8a\x9b\xe6\x9d\x83\xe9\x87\x8d'),
        ),
        migrations.AlterField(
            model_name='client',
            name='region_manager',
            field=models.ForeignKey(related_name='client_set', verbose_name=b'\xe5\xa4\xa7\xe5\x8c\xba\xe7\xbb\x8f\xe7\x90\x86RSM', blank=True, to='User.RSM'),
        ),
        migrations.AlterField(
            model_name='client',
            name='represent',
            field=models.CharField(default=b'', max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xbb\xa3\xe8\xa1\xa8'),
        ),
        migrations.AlterField(
            model_name='client',
            name='speaker_rate',
            field=models.CharField(default=b'\xe5\x8f\x82\xe4\xbc\x9a', max_length=50, verbose_name=b'\xe8\xae\xb2\xe8\x80\x85\xe7\xba\xa7\xe5\x88\xab'),
        ),
        migrations.AlterField(
            model_name='client',
            name='strong_point',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=250, verbose_name=b'\xe7\x89\xb9\xe9\x95\xbf'),
        ),
        migrations.AlterField(
            model_name='client',
            name='title',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe8\x81\x8c\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='client',
            name='unit',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=50, verbose_name=b'\xe5\x8d\x95\xe4\xbd\x8d'),
        ),
    ]
