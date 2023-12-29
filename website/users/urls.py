from . import views
from django.urls import path

# from django.contrib.auth.views import LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', views.get_user_logout, name='logout'),
    path('register/', views.UserRegistration.as_view(), name='register'),
    path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('edit/<slug:slug>/', views.UpdatePost.as_view(), name='edit'),
    path('delete/<slug:slug>/', views.DeletePost.as_view(), name='delete')
]
