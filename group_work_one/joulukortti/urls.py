from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('canvas/', views.canvas, name='canvas'),
    path('gallery/', views.gallery, name='gallery'),
    path('save_image/', views.save_image, name='save_image'),
]