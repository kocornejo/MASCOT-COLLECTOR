from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('mascots/', views.mascots_index, name='index'),
  path('mascots/<int:mascot_id>/', views.mascots_detail, name="detail"),
  path('mascots/create/', views.MascotCreate.as_view(), name='mascots_create'),
  path('mascots/<int:pk>/update/', views.MascotUpdate.as_view(), name='mascots_update'),
  path('mascots/<int:pk>/delete/', views.MascotDelete.as_view(), name='mascots_delete'),
  path('mascots/<int:mascot_id>/add_feeding/', views.add_feeding, name='add_feeding'),
  path('mascots/<int:mascot_id>/assoc_product/<int:product_id>/', views.assoc_product, name='assoc_product'),
  path('products/', views.ProductList.as_view(), name='products_index'),
  path('products/<int:pk>/', views.ProductDetail.as_view(), name='products_detail'),
  path('products/create/', views.ProductCreate.as_view(), name='products_create'),
  path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='products_update'),
  path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='products_delete'),
]

