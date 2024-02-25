from .models import Basis
from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, FormView
from basis.forms import ContactForm


def get_menu():
    menu = [{'main_title': 'Контакты', 'name': 'contact'}, {'main_title': 'О сайте', 'name': 'about'}]
    return menu


class HomePage(ListView):
    template_name = 'basis/index.html'
    context_object_name = 'all_posts'
    paginate_by = 3
    extra_context = {'title': 'Космос', 'main_title': 'Солнечная система'}

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
    extra_context = {'title': 'О сайте', 'main_title': 'Информация о сайте'}


class ContactPage(FormView):
    form_class = ContactForm
    template_name = 'basis/contact.html'
    extra_context = {'title': 'Связаться с нами', 'main_title': 'Связаться с нами'}

    def form_valid(self, form):
        return redirect('email_was_sent')


class TermsPage(TemplateView):
    template_name = 'basis/terms.html'
    extra_context = {'title': 'Пользовательское соглашение', 'main_title': 'Соглашение...'}


class PrivacyPage(TemplateView):
    template_name = 'basis/privacy.html'
    extra_context = {'title': 'Политика конфиденциальности', 'main_title': 'Политика...'}


def email_was_sent(request):
    extra_context = {'title': 'Сообщение отправлено', 'main_title': 'Получилось!'}
    return render(request, 'basis/email_was_sent.html', context=extra_context)


def page_not_found(request, exception):
    extra_context = {'title': 'Ошибка 404', 'main_title': 'Страница не найдена!'}
    return HttpResponseNotFound(render(request, 'basis/error_404.html'), content=extra_context)
