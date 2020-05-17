#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 3:10 下午
# @Author  : Leoning
# @File    : views.py

from django.http import HttpResponse

def movie(request):
    return HttpResponse("电影首页")

