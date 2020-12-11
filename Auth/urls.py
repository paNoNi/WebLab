from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

from Auth.views import register

urlpatterns = [
    path("login", auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('', views.index),
    path('register', register, name='register'),
    path('profile-<int:pk>', views.ProfileDetail.as_view())
]
