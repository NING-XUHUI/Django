"""url_params_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book import views
from django.http import HttpResponse
from django.urls import converters


def index(request):
    return HttpResponse("首页")


# url转换器默认为str
urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('book/', views.book),
    path('book/detail/<book_id>/<categary_id>', views.book_detail),
    path('book/author/', views.author_detail),
    path('book/publisher/<uuid:publisher_id>/', views.publisher_detail)
]
