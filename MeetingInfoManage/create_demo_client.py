# -*- coding: utf-8 -*-
from MeetingInfoManage.wsgi import *
from User.models import *

def main():
    test = RSM()
    test.user_name = u'左坦丽'
    test.password = 'e10adc3949ba59abbe56e057f20f883e'
    test.district = '广东'
    for i in range(101,150):
        client, not_exist = Client.objects.get_or_create(name = 'Preke_Boyce_{}'.format(str(i)))
        if not_exist:
            client.sex = 'male'
            client.job = 'doctor_{}'.format(str(i))
            client.office = 'hospital_{}'.format(str(i))
            client.major = 'doctor_{}'.format(str(i))
            client.region_manager = u'左坦丽'
            client.type = '临床'
            client.save()


    for i in range(151,200):
        client, not_exist = Client.objects.get_or_create(name='Preke_Boyce_{}'.format(str(i)))
        if not_exist:
            client.sex = 'male'
            client.job = 'doctor_{}'.format(str(i))
            client.office = 'hospital_{}'.format(str(i))
            client.major = 'doctor_{}'.format(str(i))
            client.region_manager = u'左坦丽'
            client.type = '院长'
            client.save()

    test.save()
    test = RSM.objects.get(user_name = u'左坦丽')
    print len(test.members.all())
    users = Client.objects.all()
    for user in users:
        if user.region_manager == u'左坦丽':
            test.members.add(user)


    print len(test.members.all())
    test.save()

if __name__ == '__main__':
    main()
    print 'Done!'
