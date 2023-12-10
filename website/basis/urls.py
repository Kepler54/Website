from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('post/<slug:post_slug>/', views.PostPage.as_view(), name='post'),
    path('category/<slug:category_slug>/', views.CategoryPage.as_view(), name='category'),
]
