#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 4:57 下午
# @Author  : Leoning
# @File    : urls.py


from django.urls import path
from . import views

# 应用命名空间
# appname
app_name = 'front'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login')
]
