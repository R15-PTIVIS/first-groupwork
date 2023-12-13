from django.urls import path
from . import views
from .views import ColorListView, ColorCreateView, ColorUpdateView, ColorDeleteView


urlpatterns = [
    path('', views.home, name='home'),
    path('canvas/', views.canvas, name='canvas'),
    path('gallery/', views.gallery, name='gallery'),
    path('save_drawing/', views.save_drawing, name='save_drawing'),
    path('colors/', ColorListView.as_view(), name='color_list'),
    path('colors/add/', ColorCreateView.as_view(), name='color_add'),
    path('colors/<int:pk>/edit/', ColorUpdateView.as_view(), name='color_edit'),
    path('colors/<int:pk>/delete/', ColorDeleteView.as_view(), name='color_delete'),
]