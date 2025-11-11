from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),  
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('feed/', views.feed, name='feed'),
]
