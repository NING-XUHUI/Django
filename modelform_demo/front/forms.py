#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 9:40 下午
# @Author  : Leoning
# @File    : forms.py


from django import forms
from .models import Book, User


class AddBookForm(forms.ModelForm):
    # def clean_page(self):
    #     page = self.cleaned_data.get('page')
    #     if page > 100:
    #         raise forms.ValidationError("价格不能大于1000")
    #     return page
    class Meta:
        model = Book
        fields = "__all__"
        # fields = ['title', 'page']
        # exclude = ['price']
        error_messages = {
            'page': {
                'required': "请传入page参数",
                'invalid': "请输入数字",
            },
            'price': {
                'max_value': "不得超过1000元"
            }
        }


class RegisterForm(forms.ModelForm):
    pwd1 = forms.CharField(max_length=16, min_length=6)
    pwd2 = forms.CharField(max_length=16, min_length=6)

    def clean(self):
        clean_data = super().clean()
        pwd1 = clean_data.get('pwd1')
        pwd2 = clean_data.get('pwd2')
        if pwd1 != pwd2:
            raise forms.ValidationError('密码不一致')
        else:
            return clean_data
    class Meta:
        model = User
        exclude = ['password']
