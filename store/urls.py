from django.urls import path

from . import views

urlpatterns = [
    path('products/<slug:filter>', views.products, name='products'),
    path('product/hyperspectral-tv/', views.hyperspectral_tv, name='hyperspectral_tv'),
    path('product/glass-s/', views.glass_s, name='glass_s'),
]
