from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', lambda redi: redirect('core:home')),
    path('home/', views.home, name='home'),
    path('login/', views._login, name='login'),
    path('logout/', views._logout, name='logout'),
    path('register/', views.register, name='register'),
]
