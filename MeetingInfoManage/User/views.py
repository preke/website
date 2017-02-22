# -*- coding:utf-8 -*-
from codecs import open


from django.shortcuts import render
from User.models import Client
from django.http import HttpResponse
import hashlib
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.urlresolvers import reverse
from Meeting.models import Meeting
from User.models import Client, RSM, RMM, Boss
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import *
from MeetingInfoManage.settings import *
from datetime import datetime
from django.core.servers.basehttp import FileWrapper
import csv
import os
import codecs
# Create your views here.


def getSomePage(paginator, current_num):
    num_list = list(paginator.page_range)
    if current_num - 4 < 0:
        if current_num + 4 < num_list[-1]:
            return num_list[0:6]
        else:
            return num_list[0:]
    else:
        if current_num + 3 <= num_list[-1]:
            return num_list[current_num - 3:current_num + 3]
        else:
            return num_list[num_list[-1] - 6:]


def index(request):
        if not request.session.get('user_name', False):
            return HttpResponseRedirect(reverse('login'))

        # 如果是RMM, 首页是meeting_info, 如果是rsm,首页才是 '/'
        if request.session.get('RMM', False):
            return HttpResponseRedirect(reverse('meeting_info'))

        request.session['current'] = 'index'
        if request.session.get('Boss', False):
            client_list = Client.objects.all()
        else :
            client_list = Client.objects.filter(region_manager__user_name = request.session['user_name']).order_by('name')
    # try:
        paginator = Paginator(client_list, 15)
        try:
            page = request.GET.get('page', 1)
            page_client_list = paginator.page(page)
        except PageNotAnInteger:
            page_client_list = paginator.page(1)
        except EmptyPage:
            page_client_list = paginator.page(paginator.num_pages)
        num_list = getSomePage(paginator, page_client_list)
        info = {'paginator': paginator, 'page_client_list':page_client_list, 'num_list':num_list}
        return render(request, 'User/index.html', info)
    # except:
        # return HttpResponse('error')

@csrf_exempt
def lead_in(request):
    if not request.session.get('user_name', False):
        return HttpResponseRedirect(reverse('login'))
    if request.method == 'GET':
        return render(request, 'User/client_lead_in.html')
    else :
        client = Client.objects.create()
        client.name = request.POST['name']
        client.sex = request.POST['gender']
        client.birth = request.POST['birth']
        client.job = request.POST['job']
        client.office = request.POST['office']
        client.major = request.POST['major']
        client.title = request.POST['title']
        client.unit = request.POST['unit']
        client.phone = request.POST['phone']
        client.email = request.POST['email']
        client.institute_job = request.POST['institute_job']
        client.strong_point = request.POST['string_point']
        client.speaker_rate = request.POST['jibie'] #讲者级别
        client.purpose = request.POST['aim']#参与活动目的
        client.demand = request.POST['needs']#参会需求

        rsm = RSM.objects.filter(user_name = request.POST['manager'])
        if len(rsm) > 0:
            rsm = rsm[0]
        else:
            rsm = None
        if rsm:
            client.region_manager = rsm
        client.district_manager = request.POST['d_manager']#负责地区经理
        client.represent = request.POST['repre']#负责代表
        client.type = request.POST['type']#类型
        client.potential_weight = request.POST['potential_weight']

        client.save()
        return HttpResponseRedirect(reverse('index'))

@csrf_exempt
def lead_in_extends(request):
    if not request.session.get('user_name', False):
        return HttpResponseRedirect(reverse('login'))
    if request.method == 'GET':
        return render(request, 'User/client_lead_in_extends.html')
    else :
        # try:
        # print '======================open file'
        file = request.FILES['client_lead_in_extends']
        reader = csv.reader(file)
        # print '-------------------------read file'
        # print reader.next() # cut down he head
        reader.next()
        record = reader.next()
        while True:
            # print record
            # 去掉前导和后缀空格
            record = [each.strip() for each in record]
            record = [cell.decode('gb2312','ignore').encode('utf-8') for cell in record]
            client, not_exist = Client.objects.get_or_create(name=record[0],
                                                             sex=record[1],
                                                             birth=record[2],
                                                             job=record[3],
                                                             office=record[4],
                                                             major=record[5],
                                                             title=record[6],
                                                             unit=record[7],
                                                             phone=record[8],
                                                             email=record[9],
                                                             institute_job=record[10],
                                                             strong_point=record[11],
                                                             speaker_rate=record[12],
                                                             purpose=record[13],
                                                             demand=record[14],
                                                            #  region_manager=record[15],
                                                             district_manager=record[16],
                                                             represent=record[17],
                                                             type=record[18],
                                                             potential_weight=int(record[19]),
                                                             max_potential_weight = int(record[19]))
            if (not_exist) :
                rsm = RSM.objects.filter(user_name = record[15])
                if len(rsm) > 0:
                    rsm = rsm[0]
                else:
                     rsm = None
                if rsm != None:
                    client.region_manager = rsm
                client.save()
            try:
                record = reader.next()
            except:
                break
        return HttpResponseRedirect(reverse('index'))
        # except:
            # return HttpResponse('error')


def unicode_2_gb2312(cell):
    if isinstance(cell, unicode):
        return cell.encode('gb2312')
    else :
        return cell

# 只有rsm有导出他管理的客户的信息
def lead_out(request):
    if not (request.session.get('user_name', False) and (request.session.get('RSM', False) or request.session.get('Boss', False))):
        return HttpResponseRedirect(reverse('login'))
    if request.session.get('Boss', False):
        client_list = Client.objects.all()
    else:
        rsm = RSM.objects.get(user_name = request.session['user_name'])
        client_list = Client.objects.filter(region_manager__user_name = rsm.user_name)
    # print client_list//

    relative_path = 'media/storage/'+ 'client.csv'
    csvfile = open(os.path.join(BASE_DIR, relative_path), 'w')
    #csvfile.write(codecs.BOM_UTF8)
    writer = csv.writer(csvfile)
    # strs = [u'姓名', u'性别', u'出生年月', u'职务', u'科室', u'专业', u'职称', u'单位', u'手机',
    #         u'邮箱', u'学会任职', u'特长', u'负责大区经理', u'客户潜力权重', u'主席统计', u'讲师统计']
    #姓名	性别	出生年月	职务	科室	专业	职称	单位	手机	E-mail	学会任职	特长	讲者级别	参与活动目的	参会需求	负责大区经理	负责地区经理	负责代表	类型	客户潜力权重	主席统计	讲者统计
    strs = ['姓名', '性别', '出生年月', '职务', '科室', '专业', '职称', '单位', '手机',
            'E-mail', '学会任职', '特长', '讲者级别', '参与活动目的', '参会需求', '负责大区经理', '负责地区经理',
            '负责代表', '类型', '客户潜力权重', '主席统计', '讲者统计']
    # #
    strs = [each.decode('utf-8').encode('gb2312') for each in strs]
    writer.writerow(strs)
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
        record.append(client.region_manager.user_name)
        record.append(client.district_manager)
        record.append(client.represent)
        record.append(client.type)
        record.append(client.max_potential_weight)
        record.append(client.chairman_times)
        record.append(client.speecher_times)

        record = [unicode_2_gb2312(cell) for cell in record]
        writer.writerow(record)

    csvfile.close()

    filename = os.path.join(BASE_DIR, relative_path)
    content = open(filename, "rb").read()
    # wrapper = FileWrapper(file(os.path.join(BASE_DIR, relative_path)))
    response = HttpResponse(content, content_type='application/vnd.ms-excel')
    # response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filename)
    # out_filename = 'client_'+ request.session['user_name'] + '_client.csv'
    response['Content-Disposition'] = "attachment; filename = 'client.csv' "
    return response
    # return HttpResponseRedirect(reverse('index'))


@csrf_exempt
def login(request):
    if request.method == 'GET':
        return render(request, 'User/login.html')
    else :# POST
        try:
            user_name = request.POST['user_name']
            password = request.POST['password']
            p = hashlib.md5()
            p.update(password)
            password = p.hexdigest()
            rsm = RSM.objects.filter(user_name = user_name, password = password)
            rmm = RMM.objects.filter(user_name = user_name, password = password)
            boss = Boss.objects.filter(user_name = user_name, password = password)
            info = {'state': False, 'url': reverse('login')}
            if rsm.count() > 0 :
                request.session['user_name'] = user_name
                request.session['RSM'] = 'RSM'
                info['state'] = True
                info['url'] = reverse('index')
            if rmm.count() > 0 :
                request.session['user_name'] = user_name
                request.session['RMM'] = 'RMM'
                info['state'] = True
                info['url'] = reverse('index')
            if boss.count() > 0:
                request.session['user_name'] = user_name
                request.session['Boss'] = 'Boss'
                info['state'] = True
                info['url'] = reverse('index')
            return JsonResponse(info)
        except:
            return JsonResponse({'state': False, 'url': reverse('login')})


def delete(request, client_id):
    try:
        user = Client.objects.get(id=client_id)
        user.delete()
        # user.save()
        return HttpResponseRedirect(reverse('index'))
    except:
        return HttpResponse('error')


def change_info(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'GET':
        info = {'client':client}
        return render(request, 'User/edit.html', info)
    elif request.method == 'POST':
        client.name = request.POST['name']
        client.sex = request.POST['gender']
        client.birth = request.POST['birth']
        client.job = request.POST['job']
        client.office = request.POST['office']
        client.major = request.POST['major']
        client.title = request.POST['title']
        client.unit = request.POST['unit']
        client.phone = request.POST['phone']
        client.email = request.POST['email']
        client.institute_job = request.POST['institute_job']
        client.strong_point = request.POST['string_point']
        client.speaker_rate = request.POST['jibie']  # 讲者级别
        client.purpose = request.POST['aim']  # 参与活动目的
        client.demand = request.POST['needs']  # 参会需求

        rsm = RSM.objects.filter(user_name=request.POST['manager'])
        if len(rsm) > 0:
            rsm = rsm[0]
        else:
            rsm = None
        if rsm:
            client.region_manager = rsm
        client.district_manager = request.POST['d_manager']  # 负责地区经理
        client.represent = request.POST['repre']  # 负责代表
        client.type = request.POST['type']  # 类型
        client.potential_weight = request.POST['potential_weight']

        client.save()
        return HttpResponseRedirect(reverse('index'))



def logout(request):
    del request.session['user_name']
    if request.session.get('RSM', False) :
         del request.session['RSM']
    if request.session.get('RMM', False) :
         del request.session['RMM']
    if request.session.get('Boss', False):
        del request.session['Boss']
    return HttpResponseRedirect(reverse('login'))


# 函数传参是赋值,即只是引用,不申请新的空间
def find_way_for_speecher(index, meetings, potential_weight, way, all_ways):

    if len(all_ways) > 50:
        return all_ways
    if potential_weight <= 0:
        if potential_weight < 0:
            if len(way) > 0:
                way.pop()
        # 有可能way已经在all_ways里面了, 比如, po = 5, [1, 2, 4] => [1, 2], and [1, 2, 3] => [1, 2]
        if len(way) > 0 and (not way in all_ways):
            all_ways.append(list(way))
        # print all_ways
        return all_ways
    if index >= len(meetings):
        # print index, len(meetings), '------------------------------'
        if len(way) > 0 and (not way in all_ways):
            all_ways.append(list(way))
        # print all_ways
        return all_ways
    way.append(meetings[index])
    all_ways = find_way_for_speecher(index + 1, meetings, potential_weight - meetings[index].weight_of_speecher, list(way), all_ways)
    way.pop()
    wall_ways = find_way_for_speecher(index + 1, meetings, potential_weight, list(way), all_ways)
    # print all_ways
    return all_ways

def find_way_for_participant(index, meetings, potential_weight, way, all_ways):
    if len(all_ways) > 50:
        return all_ways
    # print '------------------------------'
    if potential_weight <= 0:
        if potential_weight < 0:
            if len(way) > 0:
                way.pop()
        # 有可能way已经在all_ways里面了, 比如, po = 5, [1, 2, 4] => [1, 2], and [1, 2, 3] => [1, 2]
        if len(way) > 0 and (not way in all_ways):
            all_ways.append(list(way))
        return all_ways
    if index >= len(meetings):
        if len(way) > 0 and (not way in all_ways):
            all_ways.append(list(way))
        return all_ways
    way.append(meetings[index])
    all_ways = find_way_for_participant(index + 1, meetings, potential_weight - meetings[index].weight_of_participant, list(way), all_ways)
    way.pop()
    wall_ways = find_way_for_participant(index + 1, meetings, potential_weight, list(way), all_ways)
    return all_ways

def find_way_for_chairman(index, meetings, potential_weight, way, all_ways):
    # print '------------------------------'
    if len(all_ways) > 50:
        return all_ways
    if potential_weight <= 0:
        if potential_weight < 0:
            if len(way) > 0:
                way.pop()
        # 有可能way已经在all_ways里面了, 比如, po = 5, [1, 2, 4] => [1, 2], and [1, 2, 3] => [1, 2]
        if len(way) > 0 and (not way in all_ways):
            all_ways.append(list(way))
        return all_ways
    if index >= len(meetings):
        if len(way) > 0 and (not way in all_ways):
            all_ways.append(list(way))
        return all_ways
    way.append(meetings[index])
    all_ways = find_way_for_chairman(index + 1, meetings, potential_weight - meetings[index].weight_of_chairman, list(way), all_ways)
    way.pop()
    wall_ways = find_way_for_chairman(index + 1, meetings, potential_weight, list(way), all_ways)
    return all_ways


def choose_meeting(request, client_id):
    client = Client.objects.filter(id = client_id)[0];
    length = len(client.office)
    office_type = client.office[: length - 1]
    print office_type

    meetings = Meeting.objects.filter(is_end_up = False).filter(is_checked = False , target_client__contains = office_type).order_by('year', 'month', 'day')
    meeting_list = []
    # demand = client.demand

    
    if client.demand == u'主席':
        for each in meetings:
            if each.weight_of_chairman <= client.potential_weight:
                each.client_plan_set.filter(demand = u'主席').count() < 4
                meeting_list.append(each)
        # print meeting_list
        all_ways = find_way_for_chairman(0, meeting_list, client.potential_weight, [], [])
    elif client.demand == u'讲者':
        for each in meetings:
            if each.weight_of_speecher <= client.potential_weight:
                each.client_plan_set.filter(demand = u'讲者').count() < 4
                meeting_list.append(each)
        # print meeting_list
        all_ways = find_way_for_speecher(0, meeting_list, client.potential_weight, [], [])
    else:
        for each in meetings:
            if each.weight_of_participant <= client.potential_weight:
                each.client_plan_set.exclude(demand = u'主席').exclude(demand = u'讲者').count() < each.number_of_participant
                meeting_list.append(each)
        # print meeting_list
        all_ways = find_way_for_participant(0, meeting_list, client.potential_weight, [], [])

    def sum_of_weight(list, demand):
        weight = 0
        if demand == u'主席':
            for each in list:
                weight += each.weight_of_chairman
        elif demand == u'讲者':
            for each in list:
                weight += each.weight_of_speecher
        else:
            for each in list:
                weight += each.weight_of_participant
        return weight

    all_ways.sort(key = lambda x : sum_of_weight(x, client.demand), reverse = True)
    info = {'client': client, 'meeting_list': meeting_list, 'all_ways': all_ways}
    if request.method == 'GET' :
        return render(request, 'User/choose_meeting.html', info)
    else: # POST
        # return HttpResponse('kk')
        way_index = int(request.POST.get('way_index', 0))

        for plan_meeting in client.plan.filter(is_checked = False):
            client.plan.remove(plan_meeting)

        for meeting in all_ways[way_index]:
            client.plan.add(meeting)
        # client.plan.add(all_ways[way_index])
        return HttpResponseRedirect(reverse('client_manage'))

def client_manage(request):
    if not request.session.get('user_name', False):
        return HttpResponseRedirect(reverse('login'))
    manager_name = request.session['user_name']
    manager = RSM.objects.filter(user_name = manager_name)[0]
    users = Client.objects.all()
    # 反向查找到region_manager == manager的所有client
    client_list = manager.client_set.all()
    linChuang = client_list.filter(type = '临床').count()
    yuanZhang = client_list.filter(type = '院长').count()

    context = {'manager'  : manager,
               'linChuang': linChuang,
               'yuanZhang': yuanZhang,
               'client_list' : client_list
               }
    return render(request, 'User/manage.html', context)

def users_stat(request):
    users = Client.objects.all()
    zx = {}
    jz = {}
    for user in users:
        if user.chairman_times != 0:
            zx[user.name] = user.chairman_times
        if user.speecher_times != 0:
            jz[user.name] = user.speecher_times

    context = {'zx': zx, 'jz':jz}
    return render(request, 'User/stat.html', context)


class table_rsm:
    name = ''
    linChuang = 0
    yuanZhang = 0
    all_member = 0

    def __init__(self, n, l, y):
        self.name = n
        self.linChuang = l
        self.yuanZhang = y
        self.all_member = l + y


def rsm(request):
    rsms = RSM.objects.all()
    table = []
    for rsm in rsms:
        l = 0
        y = 0
        # print len(rsm.client_set.all())
        for user in rsm.client_set.all():
            if user.type == u'院长':
                y += 1
            elif user.type == u'临床':
                l += 1

        table.append(table_rsm(rsm.user_name, l, y))

    l_all = 0
    y_all = 0
    for user in Client.objects.all():
        if user.type == u'院长':
            y_all += 1
        elif user.type == u'临床':
            l_all += 1

    context = {
        'table': table,
        'l_all': l_all,
        'y_all': y_all,
        'all' : l_all+ y_all
    }
    return render(request, 'User/rsm.html', context)


def encry_password(password):
    p = hashlib.md5()
    p.update(password)
    return p.hexdigest()


def change_password(request):
    user_rsm = None
    user_rmm = None
    if not request.session.get('user_name', False):
        return HttpResponseRedirect(reverse('login'))

    else :
        if request.session.get('RSM', False):
            user_rsm = RSM.objects.get(user_name = request.session['user_name'])
        if request.session.get('RMM', False):
            user_rmm = RMM.objects.get(user_name = request.session['user_name'])

        if request.method == 'GET':
            return render(request, 'User/change_password.html')
        else :
            old_password = request.POST['old_password']
            new_password = request.POST['new_password']
            old_password = encry_password(old_password)
            new_password = encry_password(new_password)

            if user_rsm:
                if user_rsm.password == old_password:
                    user_rsm.password = new_password
                    user_rsm.save()
                else:
                    return render(request, 'User/error_password.html')
            if user_rmm:
                if user_rmm.password == old_password:
                    user_rmm.password = new_password
                    user_rmm.save()
                else:
                    return render(request, 'User/error_password.html')
            return HttpResponseRedirect(reverse('index'))
