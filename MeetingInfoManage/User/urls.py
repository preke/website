# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^login$', 'User.views.login', name = 'login'),
    url(r'^logout$', 'User.views.logout', name = 'logout'),
    url(r'^leadin$', 'User.views.lead_in', name = 'client_lead_in'),
    url(r'^leadin_extends$', 'User.views.lead_in_extends', name = 'client_lead_in_extends'),
    url(r'^leadout$', 'User.views.lead_out', name = 'client_lead_out'),
    url(r'^client_manage$', 'User.views.client_manage', name = 'client_manage'),
    url(r'^rsm$', 'User.views.rsm', name = 'rsm'),
    url(r'^stat$', 'User.views.users_stat', name = 'stat'),
    url(r'^choose_meeting\_(?P<client_id>[0-9]+)$', 'User.views.choose_meeting', name='choose_meeting'),
    url(r'^change_password$', 'User.views.change_password', name="change_password"),
    url(r'^delete\_(?P<client_id>[0-9]+)$', 'User.views.delete', name="delete"),
    url(r'^change_info\_(?P<client_id>[0-9]+)$', 'User.views.change_info', name="change_info"),
]
