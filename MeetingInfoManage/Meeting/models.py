# -*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from User.models import *

# Create your models here.
@python_2_unicode_compatible
class Meeting(models.Model):
    # number = models.Ch1rField('编号', max_length = 250, blank = True, default = "number")
    product = models.CharField('产品', max_length = 100, default = "")
    name_of_meeting = models.CharField('活动名称', max_length = 250, blank = True, default = "活动名称")
    rmm_of_meeting = models.CharField('会议负责人地区经理', max_length = 100, default = "")
    year =models.CharField('年', max_length=20, default='2016')
    month =models.CharField('月', max_length=20, default='1')
    day = models.CharField('日', max_length = 20, default = '1')
    city = models.CharField('活动城市', max_length=100, blank=True, default = '广州')
    type_of_meeting = models.CharField('活动类型', max_length = 100, default = '类型' )
    number_of_participant = models.IntegerField('参会人数', default = 0 )
    number_of_participant_invited = models.IntegerField('覆盖邀请人数', default = 0)
    target_client = models.CharField('目标客户群', max_length = 100, default = 0)
    # chairman = models.ManyToManyField(Client, verbose_name = '主席', related_name = 'meeting_charman_set', blank = True)
    weight_of_chairman = models.IntegerField('主席权重', default = 0)
    # speecher = models.ManyToManyField(Client, verbose_name = '讲者', related_name = 'meeting_speecher_name',blank = True)
    weight_of_speecher = models.IntegerField('讲者权重', default = 0)
    weight_of_participant = models.IntegerField('参会权重', default = 0)
    is_end_up = models.BooleanField('结束', default = False)
    is_checked = models.BooleanField('审核', default = False)
    def __unicode__(self):
        return self.name_of_meeting
    def __str__(self):
        return self.name_of_meeting
    class Meta:
        verbose_name = '会议'
        verbose_name_plural = '会议'
