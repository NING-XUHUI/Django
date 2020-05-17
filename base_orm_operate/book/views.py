from django.shortcuts import render
from .models import Book
from django.http import HttpResponse


# Create your views here.
def index(request):
    # 1.添加一条数据到数据库中
    # book = Book(name="西游记", author="吴承恩", price=100)
    # book.save()
    # 2.查询
    # 2.1根据主键查找
    # book = Book.objects.get(pk=2)
    # print(book)
    # 2.2根据其他条件查找
    # book = Book.objects.filter(name="西游记").first()
    # print(book)
    # 3.删除数据
    # book = Book.objects.get(pk=1)
    # book.delete()
    # 4.修改数据
    book = Book.objects.get(pk=2)
    book.price = 200
    book.save()
    return HttpResponse("图书添加成功")
