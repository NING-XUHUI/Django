#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 3:15 下午
# @Author  : Leoning
# @File    : views.py

from django.http import HttpResponse, StreamingHttpResponse
import csv
from django.template import loader


def index(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = "attachment;filename='abc.csv'"
    writer = csv.writer(response)
    writer.writerow(['username', 'age'])
    writer.writerow(['zhiliao', '18'])
    return response


def template_csv_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="abc.csv"'
    context = {
        'rows': [
            ['username', 'age'],
            ['zhiliao', '18'],
        ]
    }
    template = loader.get_template('abc.txt')
    csv_template = template.render(context)
    response.content = csv_template
    return response


def large_csv_view(request):
    response = StreamingHttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;filename="large.csv"'
    rows = ("Row {},{}\n".format(row, row) for row in range(0, 10000))
    print(type(rows))
    response.streaming_content = ("username,age\n", "zhiliao,19\n")
    return response
