from django.shortcuts import render
from django.views.generic import FormView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from users.context_processors import get_basis_creation
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from users.forms import UserLoginForm, UserRegisterForm, AddPostForm
from django.contrib.auth.views import LoginView, LogoutView


class AddPost(LoginRequiredMixin, FormView):
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
        return render(request, 'users/add_post.html', context=data)

    @staticmethod
    def get(request, **kwargs):
        form = AddPostForm()
        data = {
            'title': 'Добавить статью',
            'main_title': 'Добавление новой статьи',
            'form': form
        }
        return render(request, 'users/add_post.html', context=data)


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Войти',
        'main_title': 'Авторизация',
    }


def get_user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


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
