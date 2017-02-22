# -*- coding:utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
import hashlib
from Meeting.models import Meeting
from django.core.urlresolvers import reverse
# Create your models here.

def encry_password(password):
    p = hashlib.md5()
    p.update(password)
    return p.hexdigest()

# 大区经理
@python_2_unicode_compatible
class RSM(models.Model):
    user_name = models.CharField('用户名', max_length = 50, default = 'user_name')
    password = models.CharField('密码', max_length = 250, default = encry_password('123456'))
    district = models.CharField('地区', max_length = 250, default = "district")
    # members = models.ManyToManyField(Client, verbose_name = '负责的客户群', blank=True)
    def __unicode__(self):
        return self.user_name
    def __str__(self):
        return self.user_name
    class Meta:
        verbose_name = '大区经理'
        verbose_name_plural = '大区经理'

# 地区经理
@python_2_unicode_compatible
class RMM(models.Model):
    user_name = models.CharField('用户名', max_length = 250, default = 'user_name')
    password = models.CharField('密码', max_length = 250, default = encry_password('123456'))
    def __unicode__(self):
        return self.user_name
    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = '区域市场经理'
        verbose_name_plural = '区域市场经理'




@python_2_unicode_compatible
class Client(models.Model):
    name = models.CharField('姓名', max_length = 50, default = "名字")
    sex = models.CharField('性别', max_length = 10, default = "性别" , blank = True);
    birth = models.CharField('出生年月', max_length = 50, default = "无" , blank = True)
    job = models.CharField('职务', max_length = 50, default = "无" , blank = True)
    office = models.CharField('科室', max_length = 50, default = "无" , blank = True)
    major = models.CharField('专业', max_length = 50, default = "无" , blank = True)
    title = models.CharField('职称', max_length = 50, default = "无" , blank = True)
    unit = models.CharField('单位', max_length = 50, default = "无" , blank = True)
    phone = models.CharField('手机', max_length = 20, default = "无", blank = True)
    email = models.EmailField('E-mail', max_length = 50, null = True, default = '*****@163.cpm' , blank = True)
    institute_job = models.CharField('学会任职', max_length = 50, default = "无" , blank = True)
    strong_point = models.CharField('特长', max_length = 250, default = "无" , blank = True)
    # 城市级,
    speaker_rate = models.CharField('讲者级别', max_length= 50, default = '参会' )
    purpose = models.TextField('参与活动目的', default = '建立合作联系' , blank = True)
    # 参会/特色活动参会, 主席, 讲者
    demand = models.CharField('参会需求', max_length = 50, default='全国/特色活动参会')
    # region_manager = models.CharField('负责大区经理', max_length = 50, default = "")
    region_manager = models.ForeignKey(RSM, verbose_name = '大区经理RSM', related_name = 'client_set', blank = True, null = True)
    district_manager = models.CharField('负责地区经理', max_length = 50, default='温志远')
    # district_manager = models.ManyToManyField(RMM, verbose_name = '地区经理', related_name = 'rmm_district_manager_set', null = True)

    represent = models.CharField('负责代表', max_length = 50, default='' , blank = True)
    # 临床, 院长等
    type = models.CharField('类型', max_length = 50, default='临床' , blank = True)
    potential_weight = models.IntegerField('当前客户潜力权重', default = 0)
    max_potential_weight = models.IntegerField('固定客户权重', default = 0)
    chairman_times = models.IntegerField('主席统计', default = 0)
    speecher_times = models.IntegerField('讲者统计', default = 0)
    chairman_times_plan = models.IntegerField('计划主席统计', default= 0)
    speecher_times_plan = models.IntegerField('计划讲者统计', default = 0)

    # member_cover = models.IntegerField('参会覆盖', default = 0)
    attend = models.ManyToManyField(Meeting, related_name = 'client_attend_set', verbose_name = '参加的会议', blank=True)
    plan = models.ManyToManyField(Meeting, related_name='client_plan_set', verbose_name="待参加会议", blank = True)

    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('choose_meeting', args=[self.id])
    class Meta :
        verbose_name = '用户'
        verbose_name_plural = '用户'
        ordering = ['name']

@python_2_unicode_compatible
class Boss(models.Model):
    user_name = models.CharField('老板', max_length = 50, default = '老板')
    password= models.CharField('密码', max_length = 250, default = encry_password('123456'))

    def __str__(self):
        return self.user_name
    def __unicode__(self):
        return self.user_name

    class Meta:
        verbose_name = '管理员'
        verbose_name_plural= '管理员'


