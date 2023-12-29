from django.shortcuts import render
from django.views.generic import FormView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from users.context_processors import get_basis_creation, get_basis_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from users.forms import UserLoginForm, UserRegisterForm, AddPostForm
from django.contrib.auth.views import LoginView


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


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = get_basis_model()
    fields = ['post_title', 'post_content', 'photo', 'is_published', 'category']
    template_name = 'users/add_post.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Редактирование',
        'main_title': 'Редактирование статьи',
    }


class DeletePost(LoginRequiredMixin, DeleteView):
    model = get_basis_model()
    template_name = 'users/delete.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Удаление',
        'main_title': 'Удаление статьи',
    }


class UserLogin(LoginView):
    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {
        'title': 'Войти',
        'main_title': 'Авторизация',
    }


class UserRegistration(CreateView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    extra_context = {
        'title': 'Регистрация',
        'main_title': 'Регистрация'
    }
    success_url = reverse_lazy('users:login')


def get_user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
