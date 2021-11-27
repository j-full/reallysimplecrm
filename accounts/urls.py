from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('', include('django.contrib.auth.urls')),
]