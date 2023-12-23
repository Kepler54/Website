from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('login/', views.get_user_login, name='login'),
    path('logout/', views.get_user_logout, name='logout'),
    path('register/', views.get_user_registration, name='register')
]
