from django.shortcuts import render
from django.views.generic import View
from .forms import MessageBoardForm
from django.http import HttpResponse


# Create your views here.
class IndexView(View):
    def get(self, request):
        form = MessageBoardForm()
        return render(request, 'index.html', context={'form': form})

    def post(self, request):
        form = MessageBoardForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            email = form.cleaned_data.get('email')
            reply = form.cleaned_data.get('reply')
            print(title)
            print(content)
            print(email)
            print(reply)
            return HttpResponse("success")
        else:
            print(form.errors.get_json_data())
            return HttpResponse("failed")
