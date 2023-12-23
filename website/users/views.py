from django.urls import reverse
from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from users.context_processors import get_basis_creation
from django.contrib.auth import authenticate, login, logout
from users.forms import UserLoginForm, UserRegisterForm, AddPostForm


class AddPost(FormView):
    @staticmethod
    def post(request, **kwargs):
        form = AddPostForm(request.POST, request.FILES)
        if request.method == 'POST':
            if form.is_valid():
                get_basis_creation(**form.cleaned_data)
                return HttpResponseRedirect(reverse('home'))
        data = {
            'title': 'Добавить статью',
            'main_title': 'Добавление новой статьи',
            'form': form
        }
        return render(request, 'users/add_post.html', data)

    @staticmethod
    def get(request, **kwargs):
        form = AddPostForm()
        data = {
            'title': 'Добавить статью',
            'main_title': 'Добавление новой статьи',
            'form': form
        }
        return render(request, 'users/add_post.html', data)


def get_user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = UserLoginForm()
    data = {
        'title': 'Войти',
        'main_title': 'Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context=data)


def get_user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


def get_user_registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html')
    else:
        form = UserRegisterForm()
    data = {
        'title': 'Регистрация',
        'main_title': 'Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', context=data)
