from django.shortcuts import render
from datetime import datetime


def greet(world):
    return 'hello world %s' % world


def index(request):
    context = {
        'greet': greet
    }
    return render(request, 'index.html', context=context)


def add_view(request):
    context = {
        'value1': ['1', '2', '3'],
        'value2': ['4', '5', '6']
    }
    return render(request, 'add.html', context=context)


def cut_view(request):
    return render(request, 'cut.html')


def date_view(request):
    context = {
        'today': datetime.now()
    }
    return render(request, 'date.html', context=context)


def default_view(request):
    context = {
        'value': ''
    }
    return render(request, 'default.html', context=context)


def first_view(request):
    context = {
        'value': ['a', 'b', 'c']
    }
    return render(request, 'first.html', context=context)


def floatformat_view(request):
    context = {
        'value': 34.22444
    }
    return render(request, 'floatformat.html', context=context)


def join_view(request):
    context = {
        'value': ['1', '2', '3']
    }
    return render(request, 'join.html', context=context)


def length(request):
    context = {
        'value': "asdasdsaas"
    }
    return render(request, 'length.html', context=context)


def lower(request):
    context = {
        'value': "Hello World"
    }
    return render(request, 'lower.html', context=context)


# upper同lower，变大写


def random_view(request):
    context = {
        'value': [1, 2, 3, 4, 5]
    }
    return render(request, 'random.html', context=context)


def safe_view(request):
    context = {
        'value': "<script>alert('hello world');</script>"
    }
    return render(request, 'safe.html', context=context)


def slice_view(request):
    context = {
        'value': [1, 2, 3, 4, 5, 6, 7]
    }
    return render(request, 'slice.html', context=context)


def string_tags(request):
    context = {
        'value': '<script>alert("hello world)</script>'
    }
    return render(request, 'stringtags.html', context=context)


def truncatechars(request):
    context = {
        'value': '北京欢迎你'
    }
    return render(request, 'truncatechars.html', context=context)


