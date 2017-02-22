# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0005_client_attend'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='demand',
            field=models.TextField(default=b'\xe5\x85\xa8\xe5\x9b\xbd/\xe7\x89\xb9\xe8\x89\xb2\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x8f\x82\xe4\xbc\x9a', verbose_name=b'\xe5\x8f\x82\xe4\xbc\x9a\xe9\x9c\x80\xe6\xb1\x82'),
        ),
        migrations.AddField(
            model_name='client',
            name='district_manager',
            field=models.CharField(default=b'\xe6\xb8\xa9\xe5\xbf\x97\xe8\xbf\x9c', max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe5\x9c\xb0\xe5\x8c\xba\xe7\xbb\x8f\xe7\x90\x86'),
        ),
        migrations.AddField(
            model_name='client',
            name='purpose',
            field=models.TextField(default=b'\xe5\xbb\xba\xe7\xab\x8b\xe5\x90\x88\xe4\xbd\x9c\xe8\x81\x94\xe7\xb3\xbb', verbose_name=b'\xe5\x8f\x82\xe4\xb8\x8e\xe6\xb4\xbb\xe5\x8a\xa8\xe7\x9b\xae\xe7\x9a\x84'),
        ),
        migrations.AddField(
            model_name='client',
            name='represent',
            field=models.CharField(default=b'\xe6\xb8\xa9\xe5\xbf\x97\xe8\xbf\x9c', max_length=50, verbose_name=b'\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xbb\xa3\xe8\xa1\xa8'),
        ),
        migrations.AddField(
            model_name='client',
            name='speaker_rate',
            field=models.CharField(default=0, max_length=50, verbose_name=b'\xe8\xae\xb2\xe8\x80\x85\xe7\xba\xa7\xe5\x88\xab'),
        ),
        migrations.AddField(
            model_name='client',
            name='type',
            field=models.CharField(default=b'\xe4\xb8\xb4\xe5\xba\x8a', max_length=50, verbose_name=b'\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(default=b'email', max_length=50, verbose_name=b'E-mail'),
        ),
        migrations.AlterField(
            model_name='client',
            name='speecher_times',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xae\xb2\xe8\x80\x85\xe7\xbb\x9f\xe8\xae\xa1'),
        ),
    ]
