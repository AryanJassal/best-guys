from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.search_products, name='search_products'),
    path('products/<slug:filter>', views.filter_products, name='filter_products'),
    path('product/<slug:slug>/', views.product_details, name='product_details'),
    path('product/<slug:slug>/review/post/', views.new_review, name='post_review'),
    path('product/<slug:slug>/review/delete/<int:pk>', views.delete_review, name='delete_review'),
]
