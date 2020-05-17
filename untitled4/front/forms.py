#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 6:55 下午
# @Author  : Leoning
# @File    : forms.py


from django import forms


class MessageBoardForm(forms.Form):
    title = forms.CharField(max_length=100, min_length=2, label='标题', error_messages={"min_length": "最小不能少于一个字符"})
    content = forms.CharField(widget=forms.Textarea, label='内容')
    email = forms.EmailField(label='邮箱')
    reply = forms.BooleanField(required=False, label='是否回复')
