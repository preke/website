#-*- coding:utf-8 -*-
from django.shortcuts import render
from User.models import Client
from django.http import HttpResponse
import hashlib
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from Meeting.models import Meeting
from User.models import Client, RSM, RMM
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import *
from MeetingInfoManage.settings import *
import csv
import os

# Create your views here.
def index(requset):
    return HttpResponse('Under Construction.....')


def meeting_info(request):
    if not (request.session.get('user_name', False) and (request.session.get('RMM', False) or request.session.get('Boss', False))):
        return HttpResponseRedirect(reverse('login'))

    request.session['current'] = 'meeting_info'
    # client_list = Client.objects.all()
    if request.session.get('Boss', False):
        meeting_list = Meeting.objects.all()
    else:
        meeting_list = Meeting.objects.filter(rmm_of_meeting = request.session['user_name']).order_by('-year')

    try:
        paginator = Paginator(meeting_list, 15)
        try:
            page = request.GET.get('page', 1)
            page_meeting_list = paginator.page(page)
        except PageNotAnInteger:
            page_meeting_list = paginator.page(1)
        except EmptyPage:
            page_meeting_list = paginator.page(paginator.num_pages)
        info = {'paginator': paginator, 'page_meeting_list':page_meeting_list}
        return render(request, 'Meeting/meeting_info.html', info)
    except:
         return HttpResponse('error')


def lead_in(request):
    if not (request.session.get('user_name', False) and request.session.get('RMM', False)):
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'GET' :
        return render(request, 'Meeting/meeting_lead_in.html')
    else :
        try:
            meeting = Meeting.objects.create()
            meeting.product = request.POST['product']
            meeting.name_of_meeting = request.POST['name_of_meeting']
            meeting.rmm_of_meeting = request.POST['rmm_of_meeting']
            meeting.year = request.POST['year']
            meeting.month = request.POST['month']
            meeting.day = request.POST['day']
            meeting.city = request.POST['city']
            meeting.number_of_participant = request.POST['number_of_participant']
            meeting.number_of_participant_invited = request.POST['number_of_participant']
            meeting.target_client = request.POST['target_client']
            meeting.weight_of_chairman = request.POST['weight_of_chairman']
            meeting.weight_of_speecher = request.POST['weight_of_speecher']
            meeting.weight_of_participant = request.POST['weight_of_participant']

            meeting.rmm_of_meeting = request.session['user_name']
            meeting.save()
            return HttpResponseRedirect(reverse('index'))
        except:
            return HttpResponse('error');

@csrf_exempt
def lead_in_extends(request):
    if not (request.session.get('user_name', False) and request.session.get('RMM', False)):
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'GET':
        return render(request, 'Meeting/meeting_lead_in_extends.html')
    else:
        file = request.FILES['meeting_lead_in_extends']
        reader = csv.reader(file)
        reader.next() # cut down he head
        record = reader.next()
        while True :
            record = [each.strip() for each in record]
            record = [cell.decode('gb2312','ignore').encode('utf-8') for cell in record]
            # 增加数字字段的容错性
            try:
                record[8] = int(record[8])
            except:
                record[8] = 0

            try:
                record[9] = int(record[9])
            except:
                record[9] = 0

            try:
                record[15] = int(record[15])
            except:
                record[15] = 0

            try:
                record[24] = int(record[24])
            except:
                record[24] = 0

            try:
                record[25] = int(record[25])
            except:
                record[25] = 0

            meeting, not_exist = Meeting.objects.get_or_create( product = record[0],
                                                                name_of_meeting = record[1],
                                                                rmm_of_meeting = record[2],
                                                                year = record[3],
                                                                month = record[4],
                                                                day = record[5],
                                                                city = record[6],
                                                                type_of_meeting = record[7],
                                                                number_of_participant = int(record[8]),
                                                                number_of_participant_invited = int(record[9]),
                                                                target_client = record[10],
                                                                weight_of_chairman =int(record[15]),
                                                                weight_of_speecher = int(record[24]),
                                                                weight_of_participant = int(record[25]))
            if not_exist :
                meeting.rmm_of_meeting = request.session['user_name']
                meeting.save()

            try:
                record = reader.next()
            except:
                break
        return HttpResponseRedirect(reverse("index"))


def unicode_2_gb2312(cell):
    if isinstance(cell, unicode):
        return cell.encode('gb2312')
    else:
        return cell


def lead_out(request):
    if not (request.session.get('user_name', False) and (request.session.get('RMM', False) or request.session.get('Boss', False))):
        return HttpResponseRedirect(reverse('login'))
    
    if request.session.get('Boss', False):
        meeting_list = Meeting.objects.all()
    else:
        meeting_list = Meeting.objects.filter(rmm_of_meeting = request.session['user_name'])

    relative_path = 'media/storage/meeting.csv'
    csvfile = open(os.path.join(BASE_DIR, relative_path), 'wb')
    writer = csv.writer(csvfile)
    strs = ['产品',
            '活动名称',
            '活动负责人',
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
                  meeting.rmm_of_meeting,
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
        ii = 10
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

    csvfile.close()
    filename = os.path.join(BASE_DIR, relative_path)
    content = open(filename, "rb").read()
    # wrapper = FileWrapper(file(os.path.join(BASE_DIR, relative_path)))
    response = HttpResponse(content, content_type='application/vnd.ms-excel')
    # response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filename)
    out_filename = 'client_'+ request.session['user_name'] + '_meeting.csv'
    response['Content-Disposition'] = "attachment; filename = 'meeting.csv' "
    return response



def statistics(request, meeting_id):
    if request.method == 'GET':
        meeting = Meeting.objects.get(id=meeting_id)
        users = meeting.client_plan_set.all()
        context = {'meeting':meeting, 'users':users}
        return render(request, 'Meeting/static.html', context)
    elif request.method == 'POST':
        ans = request.POST.getlist('chose')
        meeting = Meeting.objects.get(id=meeting_id)
        meeting.is_end_up = True
        meeting.number_of_participant_invited = len(ans)
        meeting.save()
        for a in ans:
            user = Client.objects.get(id=a)
            user.attend.add(meeting)
            if user.demand == u'主席':
                user.chairman_times += 1
            elif user.demand == u'讲者':
                user.speecher_times += 1
            if meeting in user.plan.all():
                user.plan.remove(meeting)
            user.save()
        return HttpResponseRedirect(reverse('meeting_info'))

def check(request, meeting_id):
    if not (request.session.get('user_name', False) and request.session.get('RMM', False)):
        return HttpResponseRedirect(inverse('login'))

    rmm = RMM.objects.get(user_name = request.session['user_name'])
    meeting = Meeting.objects.get(id = meeting_id)
    client_list = meeting.client_plan_set.all()
    info = {'meeting': meeting, 'client_list': client_list, 'rmm': rmm}
    if request.method == 'GET':
        return render(request, 'Meeting/check.html', info)
    else: #POST
        meeting.is_checked = True
        for client in meeting.client_plan_set.filter(demand = u'主席'):
            # print client
            client.chairman_times_plan += 1
            client.save()
        for client in meeting.client_plan_set.filter(demand = u'讲者'):
            # print client
            client.speecher_times_plan += 1
            client.save()
        meeting.save()
        return HttpResponseRedirect(reverse('index'))


class CanHui:
    attend_linchuang = 0
    attend_yuanzhang = 0
    not_attend_linchuang = 0
    not_attend_yuanzhang = 0

    def __init__(self):
        self.attend_linchuang = 0
        self.attend_yuanzhang = 0
        self.not_attend_linchuang = 0
        self.not_attend_yuanzhang = 0


def fugai(request, id):
    meeting = Meeting.objects.get(id=id)
    users = Client.objects.all()
    attend_users = []
    for user in users:
        if meeting in user.attend.all():
            attend_users.append(user)

    dict = {}
    rsms = RSM.objects.all()
    for rsm in rsms:
        dict[rsm.user_name] = CanHui()
        dict[rsm.user_name].not_attend_linchuang = rsm.client_set.filter(type= '临床').count()
        dict[rsm.user_name].not_attend_yuanzhang = rsm.client_set.filter(type= '院长').count()



    linchuang_number = meeting.client_attend_set.all().filter(type= '临床').count()
    yuanzhang_number = meeting.client_attend_set.all().filter(type= '院长').count()
    zhongji_number = linchuang_number + yuanzhang_number

    lc_number = Client.objects.filter(type= '临床').count() - linchuang_number
    yz_number = Client.objects.filter(type= '院长').count() - yuanzhang_number
    zj_number = Client.objects.count() - zhongji_number

    for user in attend_users:
        for rsm in rsms:
            if user in rsm.client_set.all():
                if user.type == u'临床':
                    dict[rsm.user_name].attend_linchuang += 1
                    dict[rsm.user_name].not_attend_linchuang -= 1
                if user.type == u'院长':
                    #print 'kkkkkkkkkk--------------------00'
                    dict[rsm.user_name].attend_yuanzhang += 1
                    dict[rsm.user_name].not_attend_yuanzhang -= 1

    #print dict

    theme = meeting.name_of_meeting
    context = {'theme': theme, 'dict': dict, 'a':linchuang_number,
               'b':yuanzhang_number, 'c':zhongji_number, 'd':lc_number, 'e':yz_number, 'f': zj_number}
    return render(request, 'Meeting/fugai.html', context)


def edit(request, id):
    meeting = Meeting.objects.get(id=id)
    if request.method == 'GET':
        info = {'meeting':meeting}
        return render(request, 'Meeting/edit.html', info)
    elif request.method == 'POST':
        try:
            # meeting = Meeting.objects.create()
            meeting.product = request.POST['product']
            meeting.name_of_meeting = request.POST['name_of_meeting']
            meeting.year = request.POST['year']
            meeting.month = request.POST['month']
            meeting.day = request.POST['day']
            meeting.city = request.POST['city']
            meeting.number_of_participant = request.POST['number_of_participant']
            meeting.number_of_participant_invited = request.POST['number_of_participant']
            meeting.target_client = request.POST['target_client']
            meeting.weight_of_chairman = request.POST['weight_of_chairman']
            meeting.weight_of_speecher = request.POST['weight_of_speecher']
            meeting.weight_of_participant = request.POST['weight_of_participant']

            meeting.rmm_of_meeting = request.session['user_name']
            meeting.save()
            return HttpResponseRedirect(reverse('index'))
        except:
            return HttpResponse('error')
    else:
        return HttpResponse('error')


def delete_meeting(request, id):
    meeting = Meeting.objects.get(id=id)
    try:
        meeting.delete()
        return HttpResponseRedirect(reverse('index'))
    except:
        return HttpResponse('error')
