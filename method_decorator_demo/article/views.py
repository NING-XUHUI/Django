from django.shortcuts import render
from .models import Article
from django.views.decorators.http import require_http_methods, require_GET
from django.http import HttpResponse


# @require_GET = @require_http_methods(['GET'])

# @require_safe = @require_http_methods(['POST','GET'])
# Create your views here.
@require_http_methods(['GET'])
def index(request):
    # 首页是返回所有的文章
    # 只能使用get函数访问视图函数
    articles = Article.objects.all()
    return render(request, 'index.html', context={'articles': articles})


@require_http_methods(['POST', 'GET'])
def add_article(request):
    # 如果使用GET请求，返回一个添加文章的html页面
    # 如果使用POST访问，那么就获取数据并保存
    if request.method == 'GET':
        return render(request, 'add_article.html')
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        return HttpResponse("success")