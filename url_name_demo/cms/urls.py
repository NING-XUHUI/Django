#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 4:56 下午
# @Author  : Leoning
# @File    : urls.py

from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login')
]
