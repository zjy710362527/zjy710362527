from django.contrib import admin
from django.urls import path

from MyApp import views

urlpatterns = [
    path('index/', views.index),
    path('register/', views.register),
    # path('index/', views.index),
    path('login/', views.login),
    path('logout/', views.logout),
    path('dashboard/', views.dashboard, name='dashboard'),
]