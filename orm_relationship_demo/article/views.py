from django.shortcuts import render
from .models import Article, Category, Tag
from frontuser.models import FrontUser, UserExtension
from django.http import HttpResponse


# Create your views here.
def index(request):
    # article = Article(title="abc", content="111")
    # category = Category(name="最新文章")
    # category.save()
    # article.category = category
    # article.save()
    article = Article.objects.first()
    print(article.category.name)
    return HttpResponse("success")


def delete_view(request):
    category = Category.objects.get(pk=1)
    category.delete()
    return HttpResponse("success")


def one_to_many_view(request):
    # 1.one-many
    # article = Article(title="aaa", content='qwe')
    # category = Category.objects.first()
    # author = FrontUser.objects.first()
    # article.category = category
    # article.author = author
    #
    # article.save()
    # 2 获取某个分类所有文章
    category = Category.objects.first()
    # # article = category.article_set.first()
    # # print(article)
    # articles = category.articles.all()
    # for article in articles:
    #     print(article)
    article = Article(title='11111', content='333222')
    article.author = FrontUser.objects.first()
    category.articles.add(article, bulk=False)

    return HttpResponse("success")


def one_to_one_view(request):
    # user = FrontUser.objects.first()
    # extension = UserExtension(school='xatu')
    # extension.user = user
    # extension.save()
    # extension = UserExtension.objects.first()
    # print(extension.user)
    user = FrontUser.objects.first()
    print(user.extension)
    return HttpResponse("success")


def many_to_many_view(request):
    # article = Article.objects.first()
    # # tag = Tag(name="热门文章")
    # tag = Tag(name="冷门文章")
    # tag.save()
    # article.tag_set.add(tag)

    # tag = Tag.objects.get(pk=1)
    # article = Article.objects.get(pk=3)
    # tag.articles.add(article)

    article = Article.objects.get(pk=1)
    tags = article.tags.all()
    for tag in tags:
        print(tag)

    return HttpResponse("success")
