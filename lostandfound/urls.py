from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

from django.contrib import admin
from django.urls import path
from lostandfound import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
