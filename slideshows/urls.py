from django.urls import path
from . import views

urlpatterns = [
    path('', views.slideshow_list, name='slideshow_list'),
    path('<int:pk>/', views.slideshow_detail, name='slideshow_detail'),
]
