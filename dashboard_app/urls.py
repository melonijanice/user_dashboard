from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome),
    path('dashboard',views.dashboard)
]