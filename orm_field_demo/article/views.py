from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.
def index(request):
    # article = Article(removed=False)
    # article.save()
    article = Article(null=True)
    article.save()
    return HttpResponse("Success")
