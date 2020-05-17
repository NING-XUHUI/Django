#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 4:20 下午
# @Author  : Leoning
# @File    : urls.py
from django.urls import path
from . import views

app_name = 'front'

urlpatterns = [
    path('add/', views.add_article, name='add_article'),
    path('list/', views.ArticleListView.as_view(), name='article_list'),
    path('login/', views.login, name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
