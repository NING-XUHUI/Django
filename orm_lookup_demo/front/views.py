from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category


# Create your views here.
def index(request):
    article = Article.objects.filter(title__iexact="hello world")
    print(article.query)
    print(article)
    return HttpResponse("success")


def index1(request):
    article = Article.objects.filter(pk=1)
    print(article.query)
    return HttpResponse("success")


def index2(request):
    article = Article.objects.filter(title__icontains="hello world")
    # article = Article.objects.filter(title__contains="hello world")区分大小写
    print(article.query)
    print(article)
    return HttpResponse("success")


def index3(request):
    # 查找文章id为1，2，3的分类
    # articles = Article.objects.filter(id__in=[1, 2, 3])
    # for article in articles:
    #     print(article)
    # categorys = Category.objects.filter(article__in=[1, 2, 3])  # 若使用了relate_name，则应该使用relate_name进行反向查找
    # for category in categorys:
    #     print(category)
    # 所有标题包含hello的分类
    articles = Article.objects.filter(title__icontains="hello")
    categories = Category.objects.filter(article__in=articles)
    for categorie in categories:
        print(categorie)

    print(categories.query)
    return HttpResponse("success")


def index4(request):
    # articles = Article.objects.filter(id__gte=2)
    articles = Article.objects.filter(id__gt=2)
    print(articles)
    print(articles.query)
    return HttpResponse("success")


def index5(request):
    # articles = Article.objects.filter(title__startswith="hello")
    articles = Article.objects.filter(title__istartswith="hello")
    print(articles)
    print(articles.query)
    return HttpResponse("success")
