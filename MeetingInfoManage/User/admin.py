# -*- coding:utf-8
from django.contrib import admin
from User.models import *
from User.views import *
from Meeting.models import *
import csv
import hashlib

# Register your models here.

def update_user_csv_data():
    client_list = Client.objects.all()
    relative_path = 'commonStatic/storage/' + 'client.csv'
    csvfile = open(os.path.join(BASE_DIR, relative_path), 'w')
    # csvfile.write(codecs.BOM_UTF8)
    writer = csv.writer(csvfile)
    # strs = [u'姓名', u'性别', u'出生年月', u'职务', u'科室', u'专业', u'职称', u'单位', u'手机',
    #         u'邮箱', u'学会任职', u'特长', u'负责大区经理', u'客户潜力权重', u'主席统计', u'讲师统计']
    # 姓名	性别	出生年月	职务	科室	专业	职称	单位	手机	E-mail	学会任职	特长	讲者级别	参与活动目的	参会需求	负责大区经理	负责地区经理	负责代表	类型	客户潜力权重	主席统计	讲者统计
    strs = ['姓名', '性别', '出生年月', '职务', '科室', '专业', '职称', '单位', '手机',
            'E-mail', '学会任职', '特长', '讲者级别', '参与活动目的', '参会需求', '负责大区经理', '负责地区经理',
            '负责代表	', '类型', '客户潜力权重', '主席统计', '讲者统计']
    # #
    new_strs = []
    for s in strs:
        s = s.decode('utf-8').encode('gb2312')
        new_strs.append(s)

    writer.writerow(new_strs)
    for client in client_list:
        record = [client.name,
                  client.sex,
                  client.birth,
                  client.job,
                  client.office,
                  client.major,
                  client.title,
                  client.unit,
                  client.phone
                  ]
        record.append(client.email)
        record.append(client.institute_job)
        record.append(client.strong_point)
        record.append(client.speaker_rate)
        record.append(client.purpose)
        record.append(client.demand)
        record.append(client.region_manager)
        record.append(client.district_manager)
        record.append(client.represent)
        record.append(client.type)
        record.append(client.potential_weight)
        record.append(client.chairman_times)
        record.append(client.speecher_times)
        record = [unicode_2_gb2312(cell) for cell in record]

        writer.writerow(record)


    # client_list = Client.objects.all();
    # relative_path = 'static/storage/' + 'client.csv';
    # csvfile = open(os.path.join(BASE_DIR, relative_path), 'w+')
    # writer = csv.writer(csvfile)
    # writer.writerow(['姓名', '性别', '出生年月', '职务', '科室', '专业', '职称', '单位', '手机',
    #                 '邮箱', '学会任职', '特长', '讲者级别','参与活动目的','参会需求','负责大区经理', '负责地区经理',\
    #                 '代表','类型','客户潜力权重', '主席统计', '讲师统计'])
    # for client in client_list:
    #     record = [client.name, client.sex, client.birth, client.job, client.office,\
    #               client.major, client.title, client.unit, client.phone]
    #     record.append(client.email)
    #     record.append(client.institute_job)
    #     record.append(client.strong_point)
    #     record.append(client.speaker_rate)
    #     record.append(client.purpose)
    #     record.append(client.demand)
    #     record.append(client.region_manager)
    #     record.append(client.district_manager)
    #     record.append(client.represent)
    #     record.append(client.type)
    #     record.append(client.potential_weight)
    #     record.append(client.chairman_times)
    #     record.append(client.speecher_times)
    #     record = [unicode_2_gb2312(cell) for cell in record]
    #     writer.writerow(record)

class ClientAdmin(admin.ModelAdmin):
    search_fields = ['name', 'year', 'month']
    list_filter = ['name']
    # 重写save_model, 保存时调用的函数
    # obj是更新的对象, form是更新内容的表单, change是True:更新, False:新建
    def save_model(self, request, obj, form, change):
        obj.save()
        update_user_csv_data()
    def delete_model(self, request, obj):
        obj.delete()
        update_user_csv_data()


class RSMAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        str = request.POST['password']
        if len(str) == 32:
            pass
        else:
            p = hashlib.md5()
            p.update(str)
            obj.password = p.hexdigest()
        obj.save()


class RMMAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        str = request.POST['password']
        if len(str) == 32:
            pass
        else:
            p = hashlib.md5()
            p.update(str)
            obj.password = p.hexdigest()
        obj.save()


class BossAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        str = request.POST['password']
        if len(str) == 32:
            pass
        else:
            p = hashlib.md5()
            p.update(str)
            obj.password = p.hexdigest()
        obj.save()

admin.site.register(Client, ClientAdmin)

admin.site.register(RSM, RSMAdmin)

admin.site.register(RMM, RMMAdmin)

admin.site.register(Boss, BossAdmin)
