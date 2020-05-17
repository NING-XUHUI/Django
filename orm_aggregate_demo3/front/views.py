from django.shortcuts import render
from .models import Book, Author, BookOrder
from django.http import HttpResponse
from django.db.models import Avg, Count, Max, Min, Sum
from django.db import connection


# Create your views here.


def index(request):
    result = Book.objects.aggregate(Avg("price"))
    print(result)
    # print(result.query)
    print(connection.queries)
    return HttpResponse("success")


def index2(request):
    books = Book.objects.annotate(avg=Avg("bookorder__price"))
    for book in books:
        print('%s/%s' % (book.name, book.avg))
    print(connection.queries)
    return HttpResponse("success")


def index3(request):
    # result = Book.objects.aggregate(book_nums=Count("id"))
    # print(result)
    # print(connection.queries)

    # results = Author.objects.aggregate(email_nums=Count('email',distinct=True))
    # print(results)
    # print(connection.queries)

    books = Book.objects.annotate(book_nums=Count("bookorder__id"))
    for book in books:
        print('%s/%s' % (book.name, book.book_nums))
    print(connection.queries)
    return HttpResponse("success")


def index4(request):
    # result = Author.objects.aggregate(max=Max("age"),min=Min("age"))
    # print(result)
    # print(connection.queries)
    books = Book.objects.annotate(book_max=Max('bookorder__price'), book_min=Min('bookorder__price'))
    for book in books:
        print('%s/%s,%s' % (book.name, book.book_max, book.book_min))

    print(connection.queries)

    return HttpResponse("success")


def index5(request):
    # result = BookOrder.objects.aggregate(sum=Sum('price'))
    # print(result)
    # print(connection.queries)

    # books = Book.objects.annotate(sum=Sum('bookorder__price'))
    # for book in books:
    #     print('%s/%s' % (book.name, book.sum))
    #
    # print(connection.queries)

    # 求2018年年度每一本书销售总额
    return HttpResponse("success")
