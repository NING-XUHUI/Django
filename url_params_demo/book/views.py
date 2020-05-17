from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def book(request):
    return HttpResponse("图书首页")


def book_detail(request, book_id, categary_id):
    # 可以从数据库中根据book_id获取图书信息
    text = "您获取的图书id是：%s ,图书分类是：%s " % (book_id, categary_id)
    return HttpResponse(text)


def author_detail(request):
    author_id = request.GET['id']
    text = '作者的id是：%s ' % author_id
    return HttpResponse(text)


def publisher_detail(request, publisher_id):
    text = "出版社的id是：%s" % publisher_id
    return HttpResponse(text)
