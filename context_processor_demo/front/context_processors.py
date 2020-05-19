#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/19 2:26 下午
# @Author  : Leoning
# @File    : context_processors.py

from .models import User


def front_user(request):
    user_id = request.session.get('user_id')
    context = {}
    if user_id:
        try:
            user = User.objects.get(pk=user_id)
            context['front_user'] = user
        except:
            pass
    return context
