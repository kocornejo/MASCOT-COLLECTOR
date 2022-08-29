from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('mascots/', views.mascots_index, name='index'),
  path('mascots/<int:mascot_id>/', views.mascots_detail, name="detail")
]

