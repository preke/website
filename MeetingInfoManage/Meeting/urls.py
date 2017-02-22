# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^leadin$', 'Meeting.views.lead_in', name = 'meeting_lead_in'),
    url(r'leadin_extends', 'Meeting.views.lead_in_extends', name = 'meeting_lead_in_extends'),
    url(r'^leadout$', 'Meeting.views.lead_out', name = 'meeting_lead_out'),
    url(r'^meeting_info$', 'Meeting.views.meeting_info', name='meeting_info'),
    url(r'^meeting_static/(?P<meeting_id>[0-9]+)/$', 'Meeting.views.statistics', name='static'),
    url(r'^meeting_check/(?P<meeting_id>[0-9]+)/$', 'Meeting.views.check', name='check'),
    url(r'^meeting_fugai/(?P<id>[0-9]+)/$', 'Meeting.views.fugai', name='fugai'),
    url(r'^meeting_edit/(?P<id>[0-9]+)/$', 'Meeting.views.edit', name='edit'),
    url(r'^meeting_delete/(?P<id>[0-9]+)/$', 'Meeting.views.delete_meeting', name='delete_meeting'),
]
