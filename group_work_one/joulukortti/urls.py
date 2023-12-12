from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('canvas/', views.canvas, name='canvas'),
    path('gallery/', views.gallery, name='gallery'),
    path('save_drawing/', views.save_drawing, name='save_drawing')
]