from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def book(request):
    return HttpResponse("图书首页")


def book_detail(request, book_id):
    text = '图书的id是%s ' % book_id
    return HttpResponse(text)
