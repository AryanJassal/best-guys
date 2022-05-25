from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('product/hyperspectral-tv/', views.hyperspectral_tv, name='hyperspectral_tv'),
    path('product/glass-s/', views.glass_s, name='glass_s'),
]
