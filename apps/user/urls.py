#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/6 17:17
# @Author  : tanxw

from django.conf.urls import url
from . import views

urlpatterns = [
    # 首页的处理方法
    url(r'^$', views.index, name="index"),
    url(r'^login/$', views.login, name="login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^logout/$', views.logout, name="logout"),
    url(r'^confirm/$', views.user_confirm, name="confirm"),
]
