from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', lambda redi: redirect('core:home')),
    path('home/', views.home, name='home'),
]
