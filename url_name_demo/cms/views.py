from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse

# Create your views here.

def index(request):
    username = request.GET.get("username")
    if username:
        return HttpResponse('CMS首页')
    else:
        # 获取当前实例命名空间
        current_namespace = request.resolver_match.namespace
        return redirect(reverse("%s:login"%current_namespace))


def login(request):
    return HttpResponse('CMS登陆页面')
