from django.contrib import admin
from app2 import views 
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.urls import path
from .views import signup_view


urlpatterns = [
    path("signup/", signup_view, name="signup"),
    
]
