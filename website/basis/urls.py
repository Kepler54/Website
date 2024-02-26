from . import views
from django.urls import path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(views.HomePage.as_view()), name="home"),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('about/', cache_page(60)(views.AboutPage.as_view()), name='about'),
    path('post/<slug:post_slug>/', cache_page(60)(views.PostPage.as_view()), name='post'),
    path('category/<slug:category_slug>/', cache_page(60)(views.CategoryPage.as_view()), name='category'),
    path('terms/', cache_page(60)(views.TermsPage.as_view()), name='terms'),
    path('privacy/', cache_page(60)(views.PrivacyPage.as_view()), name='privacy'),
    path('email_was_sent/', views.email_was_sent, name='email_was_sent'),
    path('error_404/', views.page_not_found, name='error_404'),
]
