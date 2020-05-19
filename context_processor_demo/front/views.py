from django.shortcuts import render, redirect, reverse
from django.views.generic import View
from .forms import SignupForm, SigninForm
from .models import User
from django.contrib import messages


# Create your views here.

def index(request):
    # user_id = request.session.get('user_id')
    # context = {}
    # try:
    #     user = User.objects.get(pk=user_id)
    #     context['front_user'] = user
    # except:
    #     pass
    users = User.objects.all()
    for user in users:
        print(user)
    return render(request, 'index.html')


class SignInView(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        form = SigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.filter(username=username, password=password).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                print("密码错误")
                # messages.add_message(request, messages.INFO, '密码错误')
                messages.info(request, '密码错误')
                return redirect(reverse('signin'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('signin'))


class SignUpView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            errors = form.errors.get_json_data()
            print(errors)

            return redirect(reverse('signup'))


def blog(request):
    return render(request, 'blog.html')


def video(request):
    return render(request, 'video.html')
