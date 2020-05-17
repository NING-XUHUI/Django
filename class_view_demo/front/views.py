from django.shortcuts import render, redirect, reverse
from .models import Article
from django.http import HttpResponse
from django.views.generic import ListView, View
from django.utils.decorators import method_decorator


# Create your views here.

def add_article(request):
    articles = []
    for x in range(0, 102):
        article = Article(title='标题:%s' % x, content='内容：%s' % x)
        articles.append(article)
    Article.objects.bulk_create(articles)
    return HttpResponse("success")


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list1.html'
    context_object_name = 'articles'
    paginate_by = 10
    ordering = 'create_tiem'
    page_kwarg = 'p'

    def get_context_data(self, **kwargs):
        context = super(ArticleListView, self).get_context_data(*kwargs)
        context['username'] = 'zhiliao'
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        print(page_obj.has_next())
        print(paginator.page_range)
        pagination_data = self.get_pagination_data(paginator, page_obj)
        context.update(pagination_data)
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number
        num_pages = paginator.num_pages

        left_has_more = False
        right_has_more = False

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
        else:
            left_has_more = True
            left_pages = range(current_page - around_count, current_page)

        if current_page >= num_pages - around_count - 1:
            right_pages = range(current_page + 1, num_pages + 1)
        else:
            right_has_more = True
            right_pages = range(current_page + 1, current_page + around_count + 1)

        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'num_pages': num_pages,
        }


def login_required(func):
    def wrapper(request, *args, **kwargs):
        username = request.GET.get('username')
        if username:
            return func(request, *args, **kwargs)
        else:
            return redirect(reverse('front:login'))

    return wrapper


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
    def get(self, request):
        return HttpResponse("个人界面中心")

    #
    # def dispatch(self, request, *args, **kwargs):
    #     return super(ProfileView, self).dispatch(request, *args, **kwargs)


def login(request):
    return HttpResponse("login")
