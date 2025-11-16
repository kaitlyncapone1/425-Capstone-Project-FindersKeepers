from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('feed/', views.feed, name='feed'),
    path('main-feed/', views.main_feed, name='main_feed'),
    path('upload/', views.upload_item, name='upload'),
    path('contact/', views.about, name='contact'),
]