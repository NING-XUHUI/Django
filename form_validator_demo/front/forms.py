#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 7:29 下午
# @Author  : Leoning
# @File    : forms.py

from django import forms
from django.core import validators
from .models import User


class MyForm(forms.Form):
    # email = forms.EmailField(error_messages={'invalid': '请输入正确邮箱'})
    # price = forms.FloatField()
    # email = forms.CharField(validators=[validators.EmailValidator(message='请输入正确邮箱')])
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}')])


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    telephone = forms.CharField(validators=[validators.RegexValidator(r'1[345678]\d{9}')])
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    def clean_telephone(self):
        telephone = self.cleaned_data.get('telephone')
        exists = User.objects.filter(telephone=telephone).exists()
        if exists:
            raise forms.ValidationError(message='手机号码已被注册')

    def clean(self):

        cleaned_data = super().clean()
        pwd1 = self.cleaned_data.get('pwd1')
        pwd2 = self.cleaned_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError(message='两次密码不一致')

        return cleaned_data
