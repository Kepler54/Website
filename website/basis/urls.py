from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('post/<slug:post_slug>/', views.PostPage.as_view(), name='post'),
    path('category/<slug:category_slug>/', views.CategoryPage.as_view(), name='category'),
    path('terms/', views.TermsPage.as_view(), name='terms'),
    path('privacy/', views.PrivacyPage.as_view(), name='privacy'),
    path('email_was_sent/', views.email_was_sent, name='email_was_sent'),
]
