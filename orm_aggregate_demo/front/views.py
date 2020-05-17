from django.shortcuts import render
from .models import Author, Publisher, BookOrder, Book
from django.http import HttpResponse
from django.db.models import Avg


# Create your views here.


def index(request):
    result = Book.objects.aggregate(Avg("price"))
    return HttpResponse("success")
