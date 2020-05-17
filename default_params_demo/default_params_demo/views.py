#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 9:52 下午
# @Author  : Leoning
# @File    : views.py


from django.http import HttpResponse

book_list = [
    '三国演义',
    '水浒传',
    '西游记',
    '红楼梦'
]



def books(request, page=0):
    return HttpResponse(book_list[page])
