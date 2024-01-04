from .models import Basis
from .forms import AddContactForm
from django.urls import reverse_lazy
from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, FormView


def get_menu():
    menu = [{'main_title': 'Контакты', 'name': 'contact'}, {'main_title': 'О сайте', 'name': 'about'}]
    return menu


class HomePage(ListView):
    template_name = 'basis/index.html'
    context_object_name = 'all_posts'
    paginate_by = 3
    extra_context = {
        'title': 'Главная страница',
        'main_title': 'Солнечная система',
    }

    def get_queryset(self):
        return Basis.published.all().select_related('category')


class CategoryPage(ListView):
    template_name = 'basis/index.html'
    context_object_name = 'all_posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['all_posts'][0].category
        context['title'] = category.name
        context['main_title'] = category.name
        context['category_selected'] = category.pk
        return context

    def get_queryset(self):
        return Basis.published.filter(category__slug=self.kwargs['category_slug']).select_related('category')


class PostPage(DetailView):
    template_name = 'basis/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['post'].post_title
        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Basis.published, slug=self.kwargs[self.slug_url_kwarg])


class AboutPage(TemplateView):
    template_name = 'basis/about.html'
    extra_context = {
        'title': 'О сайте',
        'main_title': 'Информация о сайте',
    }


class ContactPage(FormView):
    form_class = AddContactForm
    template_name = 'basis/contact.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Связаться с нами',
        'main_title': 'Связаться с нами',
    }

    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)


class TermsPage(TemplateView):
    template_name = 'basis/terms.html'
    extra_context = {
        'title': 'Пользовательское соглашение',
        'main_title': 'Пользовательское соглашение',
    }


class PrivacyPage(TemplateView):
    template_name = 'basis/privacy.html'
    extra_context = {
        'title': 'Политика конфиденциальности',
        'main_title': 'Политика конфиденциальности',
    }


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена! Ошибка 404.</h1>")
