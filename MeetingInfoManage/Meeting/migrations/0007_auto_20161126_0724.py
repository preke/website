# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0011_auto_20161126_0724'),
        ('Meeting', '0006_meeting_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meeting',
            name='city_of_speecher',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='name_of_speecher',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='number',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='theme',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='type_of_meeting',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='type_of_speecher',
        ),
        migrations.RemoveField(
            model_name='meeting',
            name='weight_of_meeting',
        ),
        migrations.AddField(
            model_name='meeting',
            name='chairman',
            field=models.ManyToManyField(related_name='meeting_charman_set', verbose_name=b'\xe4\xb8\xbb\xe5\xb8\xad', to='User.Client', blank=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='day',
            field=models.CharField(default=b'1', max_length=20, verbose_name=b'\xe6\x97\xa5'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='name_of_meeting',
            field=models.CharField(default=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x90\x8d\xe7\xa7\xb0', max_length=250, verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe5\x90\x8d\xe7\xa7\xb0', blank=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='number_of_participant_invited',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xa6\x86\xe7\x9b\x96\xe9\x82\x80\xe8\xaf\xb7\xe4\xba\xba\xe6\x95\xb0'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='product',
            field=models.CharField(default=b'', max_length=100, verbose_name=b'\xe4\xba\xa7\xe5\x93\x81'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='rmm_of_meeting',
            field=models.ForeignKey(related_name='meeting_set', verbose_name=b'\xe6\xb4\xbb\xe5\x8a\xa8\xe8\xb4\x9f\xe8\xb4\xa3\xe4\xba\xba', blank=True, to='User.RMM', null=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='speecher',
            field=models.ManyToManyField(related_name='meeting_speecher_name', verbose_name=b'\xe8\xae\xb2\xe8\x80\x85', to='User.Client', blank=True),
        ),
        migrations.AddField(
            model_name='meeting',
            name='target_client',
            field=models.CharField(default=0, max_length=100, verbose_name=b'\xe7\x9b\xae\xe6\xa0\x87\xe5\xae\xa2\xe6\x88\xb7\xe7\xbe\xa4'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='weight_of_chirman',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xb8\xbb\xe5\xb8\xad\xe6\x9d\x83\xe9\x87\x8d'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='weight_of_speecher',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xae\xb2\xe8\x80\x85\xe6\x9d\x83\xe9\x87\x8d'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='month',
            field=models.CharField(default=b'1', max_length=20, verbose_name=b'\xe6\x9c\x88'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='year',
            field=models.CharField(default=b'2016', max_length=20, verbose_name=b'\xe5\xb9\xb4'),
        ),
    ]
