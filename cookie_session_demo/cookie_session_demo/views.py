#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 11:45 下午
# @Author  : Leoning
# @File    : views.py

from django.http import HttpResponse
from datetime import datetime


def index(request):
    response = HttpResponse("index")
    expires = datetime(year=2020, month=5, day=18, hour=0, minute=9, second=9)
    response.set_cookie('username', 'zhiliao', max_age=180)
    return response


def session_view(request):
    # request.session['username'] = 'zhiliao'
    # username = request.session.get('username')
    # username = request.session.get('username')
    # request.session['username'] = 'zhiliao'
    # request.session['userid'] = 10
    # request.session.clear()
    username = request.session.get('username')
    print(username)
    return HttpResponse("session_view")

