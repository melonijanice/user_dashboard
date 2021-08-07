from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('signin',views.sign_in),
    path('register',views.register),
    path('login',views.login),
    path('validate',views.validate)

]