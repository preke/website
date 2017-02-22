# -*- coding:utf-8 -*-
from django.contrib import admin
from Meeting.models import Meeting
import csv
from Meeting.views import *
# Register your models here.

def update_meeting_csv_data():
    meeting_list = Meeting.objects.all()
    relative_path = 'static/storage/meeting.csv'
    csvfile = open(os.path.join(BASE_DIR, relative_path), 'w')
    writer = csv.writer(csvfile)
    strs = ['产品',
            '活动名称',
            '年',
            '月',
            '日',
            '活动城市',
            '活动类型',
            '活动规模(参会人数)',
            'AZ覆盖邀请客户数',
            '目标客户群',
            '主席1',
            '主席2',
            '主席3',
            '主席4',
            '主席权重',
            '讲者1',
            '讲者2',
            '讲者3',
            '讲者4',
            '讲者5',
            '讲者6',
            '讲者7',
            '讲者8',
            '讲者权重',
            '参会权重']
    strs = [cell.decode('utf-8').encode('gb2312') for cell in strs]
    writer.writerow(strs)
    for meeting in meeting_list:
        chairman_list = meeting.client_attend_set.filter(demand = '主席')
        speecher_list = meeting.client_attend_set.filter(demand = '讲者')
        record = [meeting.product,
                  meeting.name_of_meeting,
                  meeting.year,
                  meeting.month,
                  meeting.day,
                  meeting.city,
                  meeting.type_of_meeting,
                  meeting.number_of_participant,
                  meeting.number_of_participant_invited,
                  meeting.target_client,
                  '',
                  '',
                  '',
                  '',
                  meeting.weight_of_chairman,
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  meeting.weight_of_speecher,
                  meeting.weight_of_participant]
        ii = 10;
        for each in chairman_list:
            if ii >= 14 :
                break
            else :
                record[ii] = each.name
                ii += 1
        ii = 15
        for each in speecher_list:
            if ii >= 23:
                break
            else:
                record[ii] = each.name
                ii += 1

        record = [unicode_2_gb2312(cell) for cell in record]
        writer.writerow(record)

class MeetingAdmin(admin.ModelAdmin):
    list_display = ['name_of_meeting', 'year','month','day','number_of_participant','number_of_participant_invited', 'is_checked','is_end_up']
    def save_model(self, request, obj, form, change):
        obj.save()
        update_meeting_csv_data()
    def delete_model(self, request, obj):
        obj.delete()
        update_meeting_csv_data()


admin.site.register(Meeting, MeetingAdmin)
