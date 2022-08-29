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
]

