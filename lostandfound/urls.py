from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('main-feed/', views.main_feed, name='main_feed'),
    path('upload/', views.upload_item, name='upload'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
]