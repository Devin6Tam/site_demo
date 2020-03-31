#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 17:17
# @Author  : tanxw

from django.conf.urls import url
from . import views

urlpatterns = [
    # 首页的处理方法
    # url(r'^$', views.index, name="index"),
    # url(r'^detail/(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    # url(r'^results/(?P<question_id>[0-9]+)/$', views.results, name="results"),
    # url(r'^vote/(?P<question_id>[0-9]+)/$', views.vote, name="vote"),
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^results/(?P<pk>[0-9]+)/$', views.ResultView.as_view(), name="results"),
    url(r'^vote/(?P<question_id>[0-9]+)/$', views.vote, name="vote"),
    url(r'^name/$', views.get_name, name="name"),
    url(r'^thanks/$', views.thanks, name="thanks"),
]
