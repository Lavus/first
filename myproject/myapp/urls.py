# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'myproject.myapp.views',
    url(r'^$', 'list', name='list'),
    url(r'^undefined$', 'undefined', name='undefined')
)

