#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/6 4:43 下午
# @Author  : Leoning
# @File    : urls.py

from django.urls import path
from book import views

urlpatterns = [
    # book/
    path('', views.book),
    path('detail/<book_id>/', views.book_detail)
]
