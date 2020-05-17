#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 3:09 下午
# @Author  : Leoning
# @File    : views.py

from django.http import HttpResponse

def book(request):
    return HttpResponse("图书首页")

