from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'blog-home'), #first arg = "blog/'nothing'" theoretically
    path('about/', views.about, name = 'blog-about'),
]